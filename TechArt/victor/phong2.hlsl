float4 FragColor; // out


// ambient
float3 ambient = ambientColor * lightColor;
	
// diffuse 
float3 norm = normalize(Normal);
float3 lightDir = normalize(lightPos - FragPos);
float diff = max(dot(norm, lightDir), 0.0);
float3 diffuse = diff * lightColor;

// specular
float3 viewDir = normalize(viewPos - FragPos);
float3 reflectDir = reflect(-lightDir, norm);  
float spec = pow(max(dot(viewDir, reflectDir), 0.0), specularPower);
float3 specular = specularStrength * specularColor * spec * lightColor;  
    
float3 result = (ambient + diffuse + specular) * objectColor;
return FragColor = float4(result, 1.0);
