static const int SceneTextureId = 14;

float2 TexelSize = View.ViewSizeAndInvSize.zw;

TexelSize *= TexelSizeScale;

float2 UV = GetDefaultSceneTextureUV(Parameters, SceneTextureId);

float3 PixelSum = float3(0, 0, 0);
float WeightSum = 0;

for (int x = -Radius; x <= Radius; x++){
for (int y = -Radius; y <= Radius; y++){

float2 Offset = UV + float2(x, y)*TexelSize;

float3 PixelColor = SceneTextureLookup(Offset, SceneTextureId, 0).rgb;

PixelSum += PixelColor;
WeightSum += 1;

}
}

return PixelSum / WeightSum;

