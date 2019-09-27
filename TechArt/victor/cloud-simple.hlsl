// CustomExpression0 - Remap
// return Ln + (V - L0) * (Hn - Ln) / (H0 - L0);
// CustomExpression1 - Density

float Transmittance = 1;
float3 LightEnergy = 0;

float4 AtmospherePos = 0;
float AtmosphereBlendLerp = 0;

bool bZeroSample = false;

int3 RandPos = int3(Parameters.SvPosition.xy, View.StateFrameIndexMod8);
float Jitter = (float(Rand3DPCG16(RandPos).x) / 0xffff);
RayPos += Jitter * RayDir;


float StepDistanceScale = clamp((length(RayPos.xy - CamPos.xy) - StepScaleDistance) / StepScaleDistance, 0, 10);

RayDir += RayDir * StepDistanceScale;

float DotLight = dot(normalize(RayDir), normalize(LightDir));

// Raymarch
for(int r = 0; r<RayMaxSteps; r++)
{
    //MipMap Scale Distance   
    //MipMap Distance Scale
    float MipMapDistanceScale = floor(length(RayPos.xy - CamPos.xy) / MipMapScaleDistance);

    /* Input
    Parameters?
    RayPos

    BaseNoiseTex/BaseNoiseTexSampler
    BaseNoiseTexTile
    SmallNoiseTex/SmallNoiseTexSampler
    SmallNoiseTexTile
    WeatherTex/WeatherTexSampler
    WeatherTexTile

    Wind
    ActorMin
    ActorMax
    MipMapDistanceScale
    LOD = 0
    */

    // CustomExpression1 - Density
    float DensitySample = CustomExpression1(Parameters, RayPos, BaseNoiseTex, BaseNoiseTexSampler, BaseNoiseTexTile, SmallNoiseTex, SmallNoiseTexSampler, SmallNoiseTexTile, WeatherTex, WeatherTexSampler, WeatherTexTile, WeatherParam, Wind, ActorMin, ActorMax, MipMapDistanceScale, 0);

    if(DensitySample > 0.01)
    {
        if(bZeroSample)
        {
            bZeroSample = false;
            RayPos -= RayDir;

            MipMapDistanceScale = floor(length(RayPos.xy - CamPos.xy) / MipMapScaleDistance);

            DensitySample = CustomExpression1(Parameters, RayPos, BaseNoiseTex, BaseNoiseTexSampler, BaseNoiseTexTile, SmallNoiseTex, SmallNoiseTexSampler, SmallNoiseTexTile, WeatherTex, WeatherTexSampler, WeatherTexTile, WeatherParam, Wind, ActorMin, ActorMax, MipMapDistanceScale, 0);
        }

        float DensityToSun = 0;
        float3 ShadowRayPos = RayPos;

        // shadow march
        for(int s = 0; s < ShadowMaxSteps; s++)
        {
            ShadowRayPos += LightDir;

            float MipMapShadowScale = floor(s / 2);// shadow

            DensityToSun += CustomExpression1(Parameters, ShadowRayPos, BaseNoiseTex, BaseNoiseTexSampler, BaseNoiseTexTile, SmallNoiseTex, SmallNoiseTexSampler, SmallNoiseTexTile, WeatherTex, WeatherTexSampler, WeatherTexTile, WeatherParam, Wind, ActorMin, ActorMax, MipMapShadowScale, 0);
        }


        

        // Attenuation
        float AttenPrim = exp(-BeerLawDensity * DensityToSun);
        float AttenSec = exp(-BeerLawDensity * AttenClampIntensity) * 0.7;
        float SunAtten = CustomExpression0(Parameters, DotLight, 0, 1, AttenSec, AttenSec * 0.5);
        float Atten = max(SunAtten, AttenPrim);


       
        float HeightGradient = (RayPos.z - ActorMin.z) / (ActorMax.z - ActorMin.z);
        float Depth = CloudOutScatterAmbient * pow(DensitySample, CustomExpression0(Parameters, HeightGradient, 0.3, 0.9, 0.5, 1.0));
        float Vertical = pow(saturate(CustomExpression0(Parameters, HeightGradient, 0.0, 0.3, 0.8, 1.0)), 0.8);
        float AmbientOutScatter = 1 - saturate(Depth * Vertical);



        float FirstHG = InScatterIntensity * ((1.0 - InScatter * InScatter) / pow(1.0 + InScatter * InScatter - 2.0 * InScatter * DotLight, 1.5)) / 4 * 3.1415;
        float SecondHG = SilverLightIntensity * pow(saturate(DotLight), SilverLightExp); 
        float InScatterHG = max(FirstHG, SecondHG);
        float OutScatterHG = ((1.0 - OutScatter * OutScatter) / pow(1.0 + OutScatter * OutScatter - 2.0 * OutScatter * DotLight, 1.5)) / 4 * 3.1415;
        float SunHighlight = lerp(InScatterHG, OutScatterHG, InOutScatterLerp);

        ///////////////////////////////////////

        float3 Light = Atten * AmbientOutScatter * SunHighlight 
        * LightIntensity * DensitySample * Transmittance;

        LightEnergy += Light;
        //LightEnergy += saturate(0.05 - pow(Light, LightPow));

        Transmittance *= 1 - DensitySample;

    }



    //Atmosphere blend

    if(AtmospherePos.w == 0)
    {
        AtmospherePos.xyz = RayPos.xyz;
        AtmospherePos.w = 1;
    }

    if(DensitySample > 0){ // density > 0
        RayPos += RayDir;
    }else{
        RayPos += RayDir * 2;
        bZeroSample = true;
    }


    if(RayPos.x > ActorMax.x || RayPos.x < ActorMin.x || RayPos.y > ActorMax.y || RayPos.y < ActorMin.y || RayPos.z > ActorMax.z || RayPos.z < ActorMin.z) 
    {
        break; 
    }


    if(Transmittance <= 0)
    {
        break;
    }

    float DepthCheck = length(WorldPosBehind - CamPos) -  length(RayPos - CamPos);

    if(DepthCheck < 0)
    {
        break;
    }

}


LightEnergy = pow(lerp(ShadowColor, LightColor, LightEnergy), LightPow);
AtmosphereBlendLerp = saturate(((length(AtmospherePos.xy - CamPos.xy) / AtmosphereBlendDistance) - 0.5) * AtmosphereBlendIntensity);
LightEnergy = lerp(LightEnergy, AtmosphereFogColor, AtmosphereBlendLerp);

return float4(LightEnergy, Transmittance);