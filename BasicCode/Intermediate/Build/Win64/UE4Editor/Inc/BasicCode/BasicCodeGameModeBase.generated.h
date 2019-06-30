// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/ObjectMacros.h"
#include "UObject/ScriptMacros.h"

PRAGMA_DISABLE_DEPRECATION_WARNINGS
#ifdef BASICCODE_BasicCodeGameModeBase_generated_h
#error "BasicCodeGameModeBase.generated.h already included, missing '#pragma once' in BasicCodeGameModeBase.h"
#endif
#define BASICCODE_BasicCodeGameModeBase_generated_h

#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_RPC_WRAPPERS
#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_RPC_WRAPPERS_NO_PURE_DECLS
#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_INCLASS_NO_PURE_DECLS \
private: \
	static void StaticRegisterNativesABasicCodeGameModeBase(); \
	friend struct Z_Construct_UClass_ABasicCodeGameModeBase_Statics; \
public: \
	DECLARE_CLASS(ABasicCodeGameModeBase, AGameModeBase, COMPILED_IN_FLAGS(0 | CLASS_Transient), CASTCLASS_None, TEXT("/Script/BasicCode"), NO_API) \
	DECLARE_SERIALIZER(ABasicCodeGameModeBase)


#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_INCLASS \
private: \
	static void StaticRegisterNativesABasicCodeGameModeBase(); \
	friend struct Z_Construct_UClass_ABasicCodeGameModeBase_Statics; \
public: \
	DECLARE_CLASS(ABasicCodeGameModeBase, AGameModeBase, COMPILED_IN_FLAGS(0 | CLASS_Transient), CASTCLASS_None, TEXT("/Script/BasicCode"), NO_API) \
	DECLARE_SERIALIZER(ABasicCodeGameModeBase)


#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_STANDARD_CONSTRUCTORS \
	/** Standard constructor, called after all reflected properties have been initialized */ \
	NO_API ABasicCodeGameModeBase(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get()); \
	DEFINE_DEFAULT_OBJECT_INITIALIZER_CONSTRUCTOR_CALL(ABasicCodeGameModeBase) \
	DECLARE_VTABLE_PTR_HELPER_CTOR(NO_API, ABasicCodeGameModeBase); \
DEFINE_VTABLE_PTR_HELPER_CTOR_CALLER(ABasicCodeGameModeBase); \
private: \
	/** Private move- and copy-constructors, should never be used */ \
	NO_API ABasicCodeGameModeBase(ABasicCodeGameModeBase&&); \
	NO_API ABasicCodeGameModeBase(const ABasicCodeGameModeBase&); \
public:


#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_ENHANCED_CONSTRUCTORS \
	/** Standard constructor, called after all reflected properties have been initialized */ \
	NO_API ABasicCodeGameModeBase(const FObjectInitializer& ObjectInitializer = FObjectInitializer::Get()) : Super(ObjectInitializer) { }; \
private: \
	/** Private move- and copy-constructors, should never be used */ \
	NO_API ABasicCodeGameModeBase(ABasicCodeGameModeBase&&); \
	NO_API ABasicCodeGameModeBase(const ABasicCodeGameModeBase&); \
public: \
	DECLARE_VTABLE_PTR_HELPER_CTOR(NO_API, ABasicCodeGameModeBase); \
DEFINE_VTABLE_PTR_HELPER_CTOR_CALLER(ABasicCodeGameModeBase); \
	DEFINE_DEFAULT_OBJECT_INITIALIZER_CONSTRUCTOR_CALL(ABasicCodeGameModeBase)


#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_PRIVATE_PROPERTY_OFFSET
#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_12_PROLOG
#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_GENERATED_BODY_LEGACY \
PRAGMA_DISABLE_DEPRECATION_WARNINGS \
public: \
	BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_PRIVATE_PROPERTY_OFFSET \
	BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_RPC_WRAPPERS \
	BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_INCLASS \
	BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_STANDARD_CONSTRUCTORS \
public: \
PRAGMA_ENABLE_DEPRECATION_WARNINGS


#define BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_GENERATED_BODY \
PRAGMA_DISABLE_DEPRECATION_WARNINGS \
public: \
	BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_PRIVATE_PROPERTY_OFFSET \
	BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_RPC_WRAPPERS_NO_PURE_DECLS \
	BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_INCLASS_NO_PURE_DECLS \
	BasicCode_Source_BasicCode_BasicCodeGameModeBase_h_15_ENHANCED_CONSTRUCTORS \
private: \
PRAGMA_ENABLE_DEPRECATION_WARNINGS


template<> BASICCODE_API UClass* StaticClass<class ABasicCodeGameModeBase>();

#undef CURRENT_FILE_ID
#define CURRENT_FILE_ID BasicCode_Source_BasicCode_BasicCodeGameModeBase_h


PRAGMA_ENABLE_DEPRECATION_WARNINGS
