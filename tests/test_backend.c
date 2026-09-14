#include <stdio.h>
#include <string.h>
#include "amistudio/backend.h"

int main(void)
{
    const AmiStudioBackendDescriptor *d = amistudio_describe_backend();

    if (d == NULL) {
        puts("FAIL: null descriptor");
        return 1;
    }
    if (d->target_api_version != AMISTUDIO_RETROSTUDIO_TARGET_API_VERSION) {
        puts("FAIL: API version mismatch");
        return 1;
    }
    if (strcmp(d->id, "amistudio") != 0) {
        puts("FAIL: backend id mismatch");
        return 1;
    }

    puts("PASS: AmiStudio backend descriptor");
    return 0;
}
