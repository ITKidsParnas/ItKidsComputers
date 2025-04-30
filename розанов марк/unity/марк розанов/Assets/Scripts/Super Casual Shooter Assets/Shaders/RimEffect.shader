Shader "CustomShaders/RimEffect"
{
	Properties
	{
		_MainColor("MainColor", Color) = (1,1,1,1)

		_MainTex("MainTexture", 2D) = "white" {}

		_RimColor("RimColor", Color) = (0, 0.5, 0.5,0)

		_RimPower("RIMPOWER", Range(0,8)) = 0.5

		_EmissionPower("EmissionPower", Range(1,10)) = 1

	}

		SubShader
		{

			Tags
		{
			"RenderType"= "Transparent"
		}
		CGPROGRAM

		#pragma surface surf Lambert

		float4 _MainColor;
		sampler2D _MainTex;

		float4 _RimColor;
		float _RimPower;
		half _EmissionPower;
		
		struct Input
		{
			float2 uv_MainTex;
			float3 viewDir;
		};

		void surf(Input IN, inout SurfaceOutput o)
		{
			o.Albedo = _MainColor.rgb;

			o.Albedo += tex2D(_MainTex , IN.uv_MainTex).rgb;

			half facing = 1 - saturate (dot(normalize(IN.viewDir), o.Normal));

			o.Emission = _RimColor.rgb * pow(facing, _RimPower);

			o.Emission = o.Emission.rgb * _EmissionPower;
		}

		ENDCG
	}

		FallBack "Diffuse"
}