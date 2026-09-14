#ifndef AMISTUDIO_BACKEND_H
#define AMISTUDIO_BACKEND_H

#ifdef __cplusplus
extern "C" {
#endif

#define AMISTUDIO_RETROSTUDIO_TARGET_API_VERSION 1u

typedef struct AmiStudioBackendDescriptor {
    unsigned int target_api_version;
    const char *id;
    const char *display_name;
    const char *backend_version;
} AmiStudioBackendDescriptor;

const AmiStudioBackendDescriptor *amistudio_describe_backend(void);

#ifdef __cplusplus
}
#endif

#endif
