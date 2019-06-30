// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "BasicCode/BasicCodeGameModeBase.h"
#ifdef _MSC_VER
#pragma warning (push)
#pragma warning (disable : 4883)
#endif
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeBasicCodeGameModeBase() {}
// Cross Module References
	BASICCODE_API UClass* Z_Construct_UClass_ABasicCodeGameModeBase_NoRegister();
	BASICCODE_API UClass* Z_Construct_UClass_ABasicCodeGameModeBase();
	ENGINE_API UClass* Z_Construct_UClass_AGameModeBase();
	UPackage* Z_Construct_UPackage__Script_BasicCode();
// End Cross Module References
	void ABasicCodeGameModeBase::StaticRegisterNativesABasicCodeGameModeBase()
	{
	}
	UClass* Z_Construct_UClass_ABasicCodeGameModeBase_NoRegister()
	{
		return ABasicCodeGameModeBase::StaticClass();
	}
	struct Z_Construct_UClass_ABasicCodeGameModeBase_Statics
	{
		static UObject* (*const DependentSingletons[])();
#if WITH_METADATA
		static const UE4CodeGen_Private::FMetaDataPairParam Class_MetaDataParams[];
#endif
		static const FCppClassTypeInfoStatic StaticCppClassTypeInfo;
		static const UE4CodeGen_Private::FClassParams ClassParams;
	};
	UObject* (*const Z_Construct_UClass_ABasicCodeGameModeBase_Statics::DependentSingletons[])() = {
		(UObject* (*)())Z_Construct_UClass_AGameModeBase,
		(UObject* (*)())Z_Construct_UPackage__Script_BasicCode,
	};
#if WITH_METADATA
	const UE4CodeGen_Private::FMetaDataPairParam Z_Construct_UClass_ABasicCodeGameModeBase_Statics::Class_MetaDataParams[] = {
		{ "HideCategories", "Info Rendering MovementReplication Replication Actor Input Movement Collision Rendering Utilities|Transformation" },
		{ "IncludePath", "BasicCodeGameModeBase.h" },
		{ "ModuleRelativePath", "BasicCodeGameModeBase.h" },
		{ "ShowCategories", "Input|MouseInput Input|TouchInput" },
	};
#endif
	const FCppClassTypeInfoStatic Z_Construct_UClass_ABasicCodeGameModeBase_Statics::StaticCppClassTypeInfo = {
		TCppClassTypeTraits<ABasicCodeGameModeBase>::IsAbstract,
	};
	const UE4CodeGen_Private::FClassParams Z_Construct_UClass_ABasicCodeGameModeBase_Statics::ClassParams = {
		&ABasicCodeGameModeBase::StaticClass,
		nullptr,
		&StaticCppClassTypeInfo,
		DependentSingletons,
		nullptr,
		nullptr,
		nullptr,
		ARRAY_COUNT(DependentSingletons),
		0,
		0,
		0,
		0x009002A8u,
		METADATA_PARAMS(Z_Construct_UClass_ABasicCodeGameModeBase_Statics::Class_MetaDataParams, ARRAY_COUNT(Z_Construct_UClass_ABasicCodeGameModeBase_Statics::Class_MetaDataParams))
	};
	UClass* Z_Construct_UClass_ABasicCodeGameModeBase()
	{
		static UClass* OuterClass = nullptr;
		if (!OuterClass)
		{
			UE4CodeGen_Private::ConstructUClass(OuterClass, Z_Construct_UClass_ABasicCodeGameModeBase_Statics::ClassParams);
		}
		return OuterClass;
	}
	IMPLEMENT_CLASS(ABasicCodeGameModeBase, 2499915306);
	template<> BASICCODE_API UClass* StaticClass<ABasicCodeGameModeBase>()
	{
		return ABasicCodeGameModeBase::StaticClass();
	}
	static FCompiledInDefer Z_CompiledInDefer_UClass_ABasicCodeGameModeBase(Z_Construct_UClass_ABasicCodeGameModeBase, &ABasicCodeGameModeBase::StaticClass, TEXT("/Script/BasicCode"), TEXT("ABasicCodeGameModeBase"), false, nullptr, nullptr, nullptr);
	DEFINE_VTABLE_PTR_HELPER_CTOR(ABasicCodeGameModeBase);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
#ifdef _MSC_VER
#pragma warning (pop)
#endif
