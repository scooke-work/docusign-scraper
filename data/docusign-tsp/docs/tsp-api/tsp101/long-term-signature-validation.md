---
title: Long term validation of PDF signatures
source_url: https://developers.docusign.com/docs/tsp-api/tsp101/long-term-signature-validation/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Trust Service Provider API
- Trust Service Provider API
- Tsp101
- Tsp101
- Long Term Signature Validation
scraped_at: '2026-06-18T22:15:24Z'
---

# Long term validation of PDF signatures

PAdES (PDF Advanced Electronic Signatures) is an [ETSI](https://www.etsi.org/) standard for applying and verifying PDF signatures. The TSP API supports the following PAdES security levels for ensuring long-term validation of your document signatures:

- **PAdES B-LT**. This profile includes verification information such as the chain of trust of the generated certificates and methods for checking revoked certificates.
- **PAdES B-LTA**. The PAdES B-LTA profile supports the PAdES B-LT profile. It also adds timestamping information and methods for checking the timestamping authority.

# PAdES B-LT example>

Code sample 1 generates a signed PDF document compliant with the PAdES B-LT security level. This example assumes that you built a CMS to support PAdES B-LT. The TSP API requires that you set the following parameters in
`completesignhash` to enable PAdES B-LT:

- `documentSecurityStore`. Embeds the verification information.
- `certificates`. Holds the certificate chain from the user
- `crls`. Holds the CRLs (certificate revocation lists) corresponding to the certificate chain.
- `ocsps`. Returns an array of OCSP servers that TSPs can use alternatively to CRLs to verify the revocation status of certificates.

```
  public async Task SignDocuments(Dictionary<string, byte[]> cmsDictionary, List<byte[]> certs, List<byte> ocsps, List<byte> crls)
{
    // Call the /signhashsession endpoint
    var signHashInfo = await tspApiClient.SignHashSessionInfo();

    var docUpdateInfos = new List<DocumentUpdateInfo>();
    foreach (var contentInfo in _contentInfoDict)
    {
        docUpdateInfos.Add(
            new DocumentUpdateInfo()
            {
                Data = contentInfo.Value,
                DocumentId = contentInfo.Key,
                ReturnFormat = "CMS",
                DocumentSecurityStore = new DocumentSecurityStore()
                {
                    Certificates = certs,
                    Ocsps = ocsps,
                    Crls = crls,
                },
            }
        );
    }

    var completeSignHashRequest = new CompleteSignRequest()
    {
        DocumentUpdateInfos = docUpdateInfos,
        CorrelationId = Guid.NewGuid(),
    };

    // Call the /completesignhash endpoint
    var completeSignHashResponse = await this._tspApiClient.CompleteSignHashSessionInfo(completeSignHashRequest);
}
```

**Code sample 1**: sign a PDF document with PAdES using the B-LT security level

# PAdES B-LTA example

Code sample 2 generates a signed PDF document compliant with the PAdES B-LTA security level. This example assumes that you built a CMS to support PAdES B-LT.

PAdES B-LTA adds timestamping verification to the PAdES B-LT level. The TSP API uses the
`completesignhash` request to generate timestamping information. You must submit the timestamping generation request after creating the last signature in the transaction.

To trigger timestamping, you must first set the
`timeStampField` field parameter to an empty JSON object value (“{}”) in the
`completesignhash` request that creates the last signature of the transaction. Next, you must submit a new
`completesignhash`request for generating the timestamping information. The value of the
`documentId` parameter must correspond to the value of the
`documentId` parameter returned by the response to the previous
`completesignhash`, which is the request that generates the last signature of the transaction. Note also that the
`remainingSignatureRequests` parameter of the response returns 1, which designates one remaining
`completesignhash` request.

```
  public async Task SignDocuments(Dictionary<string, byte[]> cmsDictionary, List<byte[]> certs, List<byte> ocsps, List<byte> crls)
{
    // Call the /signhashsession endpoint
    var signHashInfo = await tspApiClient.SignHashSessionInfo();

var docUpdateInfos = new List<DocumentUpdateInfo>();
foreach (var contentInfo in _contentInfoDict)
{
    docUpdateInfos.Add(
        new DocumentUpdateInfo()
        {
            Data = contentInfo.Value,
            DocumentId = contentInfo.Key,
            ReturnFormat = "CMS",
            DocumentSecurityStore = new DocumentSecurityStore()
            {
                Certificates = certs,
                Ocsps = ocsps,
                Crls = crls,
            },
            TimeStampField = "", // Ask the TSP API to allow a timestamp after the signature.
        }
    );
}
var completeSignHashRequest = new CompleteSignRequest()
{
    DocumentUpdateInfos = docUpdateInfos,
    CorrelationId = Guid.NewGuid(),
};

// Call the /completesignhash endpoint
var completeSignHashResponse = await this._tspApiClient.CompleteSignHashSessionInfo(completeSignHashRequest);

// Because we asked the TSP API to allow a timestamp after the signature,
// we expect there to be 1 remaining signature request in
// completeSignHashResponse.RemainingSignatureRequests
var documentUpdateInfos = new List<DocumentUpdateInfo>();
foreach (var doc in completeSignHashResponse.Documents)
{
    var hashToTimestamp = doc.Data;

    // Call the timestamper
    var timestamp = await _timestampClient.TimestampHash(hashToTimestamp);

    documentUpdateInfos.Add(new DocumentUpdateInfo()
    {
        Data = timestamp,
        ReturnFormat = "CMS",
        DocumentId = doc.DocumentId,
    });
}

var completeSignHashReqeuest = new CompleteSignRequest()
{
    DocumentUpdateInfos = documentUpdateInfos,
    CorrelationId = Guid.NewGuid(),
};

// Call the /completesignhash endpoint a second time to complete the timestamp
await _tspApiClient.CompleteSignHashSessionInfo(completeSignHashReqeuest);
}
```

**Code sample 2**: sign a PDF document with PAdES using the B-LTA security level

## Related links

[What is long term validation?](https://support.docusign.com/s/articles/What-is-Long-Term-Validation-LTV?language=en_US&rsc_301)

[![Footer: Platform 101: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/1B2IgSQD94ohLe7UVvJ5AU/ef33d80a2fbfcf734362995ffd43a438/footer-icon-1.svg)

Platform 101

Get up to speed on our concepts and platform](https://developers.docusign.com/platform/build-integration/)[Learn More](https://developers.docusign.com/platform/build-integration/)[![Footer: Stack Overflow: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/4gZwid50MSnlXqHMTZLCdV/4cc92d22086124f2f622c781cb554844/footer-icon-2.svg)

Docusign Community

Get answers from our API experts and community](https://community.docusign.com/developer-59)[Learn More](https://community.docusign.com/developer-59)[![Footer: GitHub: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/208FBzUKngjwdVfL0wAgd7/f6ff4fd8071196e37c5cac5f4f12c38c/footer-icon-3.svg)

GitHub

Find our SDKs and other source code](https://github.com/docusign)[Learn More](https://github.com/docusign)[![Footer: Partner Directory: Pre-Footer - Icon](https://images.ctfassets.net/aj9z008chlq0/2YWAk0yl09YARzBDgoq6dN/48d159475098419d1da9b3fcf14a4791/footer-icon-4.svg)

Partner Directory

See the full directory of Docusign partners](https://partners.docusign.com/s/partnerfinder)[Learn More](https://partners.docusign.com/s/partnerfinder)

[![Docusign.com](https://developers.docusign.com/img/docusign-logo.svg)](https://docusign.com)

[![X](https://images.ctfassets.net/aj9z008chlq0/jUnMYaPzapgZma42YHdEv/375916f63ce5f10c79da650018f8cb0c/x-logo.png)](https://x.com/DocusignDevs)[![youtube](https://images.ctfassets.net/aj9z008chlq0/pYBeoyZ3yAWrQ7yx2MV6U/c3e2679fb091dd6f6dbf9b250bd5ed9a/social-icon-youtube.png)](https://www.youtube.com/@DocusignDevs)[![linkedin](https://images.ctfassets.net/aj9z008chlq0/5dZh3hbAdZ97DYDNdhijTA/19230fd1c70b76dea1eef8834779e2cd/social-icon-linkedin.png)](https://www.linkedin.com/showcase/docusigndevs/)

APIs- [eSignature API](https://developers.docusign.com/docs/esign-rest-api/)
- [Web Forms API](https://developers.docusign.com/docs/web-forms-api/)
- [Workflow Builder API](https://developers.docusign.com/docs/workflow-builder-api/)
- [Agreement Manager API](https://developers.docusign.com/docs/agreement-manager-api/)
- [Docusign Admin API](https://developers.docusign.com/docs/admin-api/)
- [View all](https://developers.docusign.com/docs/)

Featured Content- [Quickstart](https://developers.docusign.com/docs/esign-rest-api/quickstart/)
- [Sample Apps](https://developers.docusign.com/sample-apps/)
- [Authentication](https://developers.docusign.com/platform/auth/)
- [Webhooks](https://developers.docusign.com/platform/webhooks/)
- [Go-Live](https://developers.docusign.com/platform/go-live/)
- [SDKs](https://developers.docusign.com/docs/sdks/)

Help- [Support](https://developers.docusign.com/support/)
- [FAQs](https://support.docusign.com/s/articles/DocuSign-Developer-Support-FAQs)

More- [Partner With Us](https://developers.docusign.com/partner/)
- [Docusign University](https://developers.docusign.com/training/)
- [Trust Center](https://www.docusign.com/trust)
- [Trust Portal](https://www.docusign.com/trust-portal)
- [ISV integration guides](https://developers.docusign.com/partner/isv-integration-guides/)

[![X](https://images.ctfassets.net/aj9z008chlq0/jUnMYaPzapgZma42YHdEv/375916f63ce5f10c79da650018f8cb0c/x-logo.png)](https://x.com/DocusignDevs)[![youtube](https://images.ctfassets.net/aj9z008chlq0/pYBeoyZ3yAWrQ7yx2MV6U/c3e2679fb091dd6f6dbf9b250bd5ed9a/social-icon-youtube.png)](https://www.youtube.com/@DocusignDevs)[![linkedin](https://images.ctfassets.net/aj9z008chlq0/5dZh3hbAdZ97DYDNdhijTA/19230fd1c70b76dea1eef8834779e2cd/social-icon-linkedin.png)](https://www.linkedin.com/showcase/docusigndevs/)

© 2024 Docusign, Inc.

[Docusign.com](https://docusign.com)

[Terms of Use](https://www.docusign.com/company/terms-and-conditions/developers)

[Privacy Notice](https://www.docusign.com/company/privacy-policy)

[Notice to California Residents](https://www.docusign.com/privacy#8)

[Intellectual Property](https://www.docusign.com/IP)

![ccpa-opt-out](https://developers.docusign.com/img/svg/ccpa-opt-out.svg)
