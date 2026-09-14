#include "amistudio/backend.h"

static const AmiStudioBackendDescriptor descriptor = {
    AMISTUDIO_RETROSTUDIO_TARGET_API_VERSION,
    "amistudio",
    "AmiStudio Amiga Backend",
    "0.0.0-m0"
};

const AmiStudioBackendDescriptor *amistudio_describe_backend(void)
{
    return &descriptor;
}
