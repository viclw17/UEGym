// CustomExpression0 - Remap
// return Ln + (V - L0) * (Hn - Ln) / (H0 - L0);

float ResultNoise = 0;
float HeightGradient = (RayPos.z - ActorMin.z) / (ActorMax.z - ActorMin.z);


//Base Noise - 3D BaseNoiseTex
float3 BaseNoiseUVW = (frac(RayPos / BaseNoiseTexTile + Wind));
float4 BaseNoise = BaseNoiseTex.SampleLevel(BaseNoiseTexSampler, BaseNoiseUVW, LOD);

//Small Noise - 3D SmallNoiseTex
float3 SmallNoiseUVW = (frac(RayPos / SmallNoiseTexTile + Wind * 10));
float4 SmallNoise = SmallNoiseTex.SampleLevel(SmallNoiseTexSampler, SmallNoiseUVW, LOD);

//Coverage texture - 2D - WeatherTex WeatherMap
float2 WeatherMapUV = RayPos.xy / WeatherTexTile + Wind.xy * 0.15;
float4 WeatherMap = WeatherTex.SampleLevel(WeatherTexSampler, WeatherMapUV, 0);
// ???
WeatherMap.b = saturate(WeatherMap.b + ((WeatherParam.r - 0.5) * 2)); 
float WeatherState = max(WeatherMap.r, saturate(WeatherParam.r - 0.5) * 2 * WeatherMap.g);

float ShapeAltering = 
saturate(CustomExpression0(Parameters, HeightGradient, 0, 0.07, 0, 1)) * 
saturate(CustomExpression0(Parameters, HeightGradient, WeatherMap.b * 0.2, WeatherMap.b, 1, 0)); // B

float DensityAltering = WeatherParam.g * HeightGradient * 
saturate(CustomExpression0(Parameters, HeightGradient, 0, 0.15, 0, 1)) * 
saturate(CustomExpression0(Parameters, HeightGradient, 0.9, 1, 1, 0)) * WeatherMap.a * 2; // A



float BaseNoiseSample = CustomExpression0(Parameters, BaseNoise.r, (BaseNoise.g * 0.625 + BaseNoise.b * 0.25 + BaseNoise.a * 0.125) - 1, 1, 0, 1);
float SmallNoiseSample = SmallNoise.r * 0.625 +  SmallNoise.g * 0.25 +  SmallNoise.b * 0.125;
float DetailNoise = 0.35 * exp(-WeatherParam.r * 0.75) * lerp(SmallNoiseSample, 1 - SmallNoiseSample, saturate(HeightGradient * 10));
float ShapeNoise = saturate(CustomExpression0(Parameters, BaseNoiseSample * ShapeAltering, 1 - WeatherParam.r * WeatherState, 1, 0, 1));

ResultNoise = saturate(CustomExpression0(Parameters, ShapeNoise, DetailNoise, 1, 0, 1)) * DensityAltering;

return ResultNoise; // float