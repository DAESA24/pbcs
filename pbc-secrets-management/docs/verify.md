---
title: "1Password Developer"
source_url: "https://developer.1password.com/docs/cli/verify/"
captured: 2025-12-15
category: concepts
relevance:
  - script integration
  - authentication
keywords:
  - 1password-cli
related: []
---

# 1Password Developer

To confirm the authenticity of 1Password CLI, the tool and all its updates are digitally signed and offered exclusively by 1Password. Always get updates directly from 1Password, and always [check to make sure that you have the latest version](https://developer.1password.com/docs/cli/reference/update/).
  * Mac
  * Windows


### ZIP file[​](https://developer.1password.com/docs/cli/verify/#zip-file "Direct link to ZIP file")
To confirm that the contents of the 1Password CLI ZIP file are authentic, unzip the file, then run the following command in the unzipped folder:
gpg --keyserver keyserver.ubuntu.com --receive-keys 3FEF9748469ADBE15DA7CA80AC2D62742012EA22
gpg --verify op.sig op
### Package file[​](https://developer.1password.com/docs/cli/verify/#package-file "Direct link to Package file")
To confirm the 1Password CLI installer file is authentic, you can verify the digital signature before installation.
  1. Open the 1Password CLI installer. If you see "This package will run a program to determine if the software can be installed", select **Continue**. This will not begin the installation.
  2. Select the lock 
  3. Select **Developer ID Installer: AgileBits Inc. (2BUA8C4S2C)**. If you see a different developer ID, or the certificate doesn't have a green checkmark indicating that it's valid, don't install the package.
  4. Select the triangle next to Details and scroll down.
  5. Make sure that the SHA-256 fingerprint in the installer matches one of the following fingerprints. If they match, the signature is verified. Select **OK** and continue installation.


![The 1Password CLI installer window showing the developer ID and fingerprints.](https://developer.1password.com/img/cli/cli-fingerprint-2025.png)
Hash | Fingerprint  
---|---  
SHA‑256 | CA B5 78 06 1B 02 09 FB 70 93 4D A3 44 EF 6F EB CD 32 79 B1 C0 74 C5 4B 0D 7D 55 57 43 B9 D8 9F  
SHA‑256 | 14 1D D8 7B 2B 23 12 11 F1 44 08 49 79 80 07 DF 62 1D E6 EB 3D AB 98 5B C9 64 EE 97 04 C4 A1 C1  
The installer automatically verifies the files in the package. If any file has an issue, installation stops without changes to your system, and you'll see a message that the installer encountered an error.
To confirm the 1Password CLI installer for Windows is authentic, verify that the signing certificate for `op.exe` was issued to AgileBits by Microsoft Corporation, and that the 
  1. Open PowerShell as an Administrator.
  2. Verify that the certificate was issued to AgileBits:
Get-AuthenticodeSignature -FilePath .\op.exe | Select-Object -ExpandProperty SignerCertificate | Select-Object Subject
See result...
Subject
-------
CN=Agilebits, O=Agilebits, L=Toronto, S=Ontario, C=CA
  3. Verify the certificate was issued by Microsoft Corporation:
Get-AuthenticodeSignature -FilePath .\op.exe | Select-Object -ExpandProperty SignerCertificate | Select-Object Issuer
See result...
Issuer
------
CN=Microsoft ID Verified CS AOC CA 02, O=Microsoft Corporation, C=US
  4. Verify the EKU matches 1Password's EKU of `1.3.6.1.4.1.311.97.661420558.769123285.207353056.500447802`:
Get-AuthenticodeSignature -FilePath .\op.exe | Select-Object -ExpandProperty SignerCertificate | Select-Object -ExpandProperty EnhancedKeyUsageList
See result...
FriendlyName ObjectId
------------ --------
1.3.6.1.4.1.311.97.1.0
Code Signing 1.3.6.1.5.5.7.3.3
1.3.6.1.4.1.311.97.661420558.769123285.207353056.500447802


### Was this page helpful?
YesNo
