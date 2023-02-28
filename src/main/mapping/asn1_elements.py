from src.generated_code.asn1.GSMA.SGP_22 import sgp_22_mapping
from src.generated_code.asn1.TCA.eUICC_Profile_Package import epp_mapping

sgp_22_tags = {
    'BF20': ['GetEuiccInfo1Request', 'EUICCInfo1'],
    'BF21': ['PrepareDownloadRequest', 'PrepareDownloadResponse'],
    'BF22': ['GetEuiccInfo2Request', 'EUICCInfo2'],
    'BF23': ['InitialiseSecureChannelRequest'],
    'BF24': ['ConfigureISDPRequest'],
    'BF25': ['StoreMetadataRequest'],
    'BF26': ['ReplaceSessionKeysRequest'],
    'BF27': ['Reserved'],
    'BF28': ['ListNotificationRequest', 'ListNotificationResponse'],
    'BF29': ['SetNicknameRequest', 'SetNicknameResponse'],
    'BF2A': ['UpdateMetadataRequest'],
    'BF2B': ['PendingNotificationsListRequest', 'PendingNotificationsListResponse'],
    'BF2D': ['ProfileInfoListRequest', 'ProfileInfoListResponse'],
    'BF2E': ['GetEuiccChallengeRequest', 'GetEuiccChallengeResponse'],
    'BF2F': ['NotificationMetadata'],
    'BF30': ['NotificationSentRequest', 'NotificationSentResponse'],
    'BF31': ['EnableProfileRequest', 'EnableProfileResponse'],
    'BF32': ['DisableProfileRequest', 'DisableProfileResponse'],
    'BF33': ['DeleteProfileRequest', 'DeleteProfileResponse'],
    'BF34': ['EuiccMemoryResetRequest', 'EuiccMemoryResetResponse'],
    'BF35': ['LoadCRLRequest and LoadCRLResponse'],
    'BF36': ['BoundProfilePackage'],
    'BF37': ['ProfileInstallationResult'],
    'BF38': ['AuthenticateServerRequest', 'AuthenticateServerResponse'],
    'BF39': ['InitiateAuthenticationRequest', 'InitiateAuthenticationResponse'],
    'BF3A': ['GetBoundProfilePackageRequest', 'GetBoundProfilePackageResponse'],
    'BF3B': ['AuthenticateClientRequest', 'AuthenticateClientResponse'],
    'BF3C': ['EuiccConfiguredAddressesRequest', 'EuiccConfiguredAddressesResponse'],
    'BF3D': ['handleNotification'],
    'BF3E': ['GetEuiccDataRequest', 'GetEuiccDataResponse'],
    'BF3F': ['SetDefaultDpAddressRequest', 'SetDefaultDpAddressResponse'],
    'BF40': ['AuthenticateClientResponseEs11'],
    'BF41': ['CancelSessionRequest', 'CancelSessionResponse', 'cancelSessionRequestEs9', 'cancelSessionResponseEs9'],
    'BF42': ['LpaeActivationRequest', 'LpaeActivationResponse'],
    'BF43': ['GetRatRequest', 'GetRatResponse'],
    'E3': ['ProfileInfo'],
}

all_mapping = {**sgp_22_mapping, **epp_mapping}

all_tags_mapping = {**sgp_22_tags}
