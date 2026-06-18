---
title: Fast-track your extension apps with reference implementations
source_url: https://www.docusign.com/blog/developers/fast-track-your-extension-apps-with-reference-implementations
site: www.docusign.com
breadcrumb:
- Home
- Home
- Blog
- Blog
- Code Examples
- Code Examples
scraped_at: '2026-06-18T18:27:13Z'
---

[Blog](https://www.docusign.com/blog)

# Fast-track your extension apps with reference implementations

[![Author Karissa Jacobsen](https://images.ctfassets.net/9pvazpst9iwl/56GSAsknmGi0EtIB92ylgp/8175ea8eb46c4f2ba06d9d41b6d3d7b1/Karissa_Jacobsen?fm=avif&q=90&w=500)

Karissa JacobsenDeveloper Advocate](https://www.docusign.com/blog/author/karissa-jacobsen)•Updated Jun 11, 2025

---

Summary•5 min read

Our new reference implementations accelerate extension app development by providing comprehensive guidance and practical examples of requirements and best practices. Watch the videos, clone the GitHub repos, and get coding!

![](https://images.ctfassets.net/9pvazpst9iwl/6BtcUgvP9lQJBE08wsAudp/86b054b14b373b5216318892fcceeb27/illustration-isometric_cube-movement_inkwell.png?fm=avif&q=90&w=500)

[Extension apps](https://developers.docusign.com/extension-apps/) are a powerful way to extend the Docusign platform with custom functionality. These apps enable developers to integrate external APIs directly into a Docusign workflow, making Docusign more adaptable to various business needs. Extension apps function by defining [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/) and corresponding [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/) that activate at designated moments during the Docusign agreement process. When these actions are triggered, the extension app communicates with an external API, and the resulting response is seamlessly incorporated back into the Docusign workflow.

To assist developers in getting started with building extension apps, we are excited to introduce our extension app [reference implementations](https://developers.docusign.com/tools/reference-implementations/). These are downloadable GitHub projects that showcase the three main extension types currently supported by Docusign. Each implementation includes a pre-built manifest file that can be directly uploaded to the Developer Console, allowing developers to instantly test the functionality of each extension type without having to configure the manifest or project from scratch.

- [**Connected Fields** opens in a new tab](https://github.com/docusign/extension-app-connected-fields-reference-implementation): This extension enables real-time custom data verification in eSignature envelopes. Unlike data verification extensions that target specific values (such as bank accounts or addresses), the connected fields extension can verify any data against your organization’s system of record.
  [View hosted manifest files for connected fields opens in a new tab](https://github.com/docusign/extension-app-connected-fields-reference-implementation/tree/main/manifests/hosted)
- [**Data IO** opens in a new tab](https://github.com/docusign/extension-app-data-io-reference-implementation): This extension enables developers to incorporate data reading and writing operations into a custom [Maestro workflow](https://developers.docusign.com/extension-apps/workflows/), enabling seamless integration of data exchanges during the signing process.
  [View hosted manifest files for data IO opens in a new tab](https://github.com/docusign/extension-app-data-io-reference-implementation/tree/main/manifests/hosted)
- [**Data Verification** opens in a new tab](https://github.com/docusign/extension-app-data-verification-reference-implementation): This is a set of extensions that enable real-time validation of critical fields, including bank account details, bank account ownership, business Federal Employer Identification Numbers (FEIN), email addresses, phone numbers, postal addresses, and Social Security Numbers.
  [View hosted manifest files for data verification opens in a new tab](https://github.com/docusign/extension-app-data-verification-reference-implementation/tree/main/manifests/hosted)

These reference implementations accelerate extension app development by providing comprehensive guidance and practical examples of requirements and best practices. To [build an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/), you must either [use the form-based experience](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/) or create an [extension app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/) file that outlines the app’s metadata, [connections](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/), [extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/), and [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/). Each reference implementation includes an example manifest that serves as a guide for developers, illustrating how to accurately define these components based on the [schema](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) established by Docusign (see sample code below). This example manifest will guide developers through configuring a sample OAuth connection and defining the required actions for each extension type. Additionally, each action is governed by a specific action contract that outlines the format for sending requests and the expected structure for receiving responses. Developers must ensure their extension apps handle data according to these contracts to ensure compatibility with the Docusign environment. The reference implementations demonstrate how to properly handle data by defining the correct request and response objects that align with the action contracts outlined in the documentation available on the Developer Center.

Here’s the example app manifest from the Connected Fields reference implementation:

```
{
    "name": "Connected Fields App",
    "description": {
        "short": "App for Connected Fields",
        "long": "This app is designed to allow users to use connected fields extensions"
    },
    "termsOfServiceUrl": "https://www.johndoe.com/tos",
    "privacyUrl": "https://www.johndoe.com/privacy-security",
    "supportUrl": "https://www.johndoe.com/support",
    "publisher": {
        "name": "John Doe",
        "email": "john.doe@gmail.com",
        "phone": "800-867-5309",
        "website": "https://www.johndoe.com"
    },
    "connections": [
        {
            "name": "authentication",
            "description": "Secure connection to the connected fields proxy",
            "type": "oauth2",
            "params": {
                "provider": "CUSTOM",
                "clientId": "<CLIENT_ID>",
                "clientSecret": "<CLIENT_SECRET>",
                "scopes": [],
                "customConfig": {
                    "authorizationMethod": "header",
                    "authorizationParams": {
                        "prompt": "consent",
                        "access_type": "offline"
                    },
                    "authorizationUrl": "<PROXY_BASE_URL>/api/oauth/authorize",
                    "requiredScopes": [],
                    "scopeSeparator": " ",
                    "tokenUrl": "<PROXY_BASE_URL>/api/oauth/token",
                    "refreshScopes": []
                }
            }
        }
    ],
    "icon": {
        "data": "iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAABQVBMVEUAAAD/AACAAP//gID/VVX/Zmb/SUn/VVX/XV3/VVVLAP//S0v/UVFOAP//Tk7/VVX/UFD/VVX/U1P/UVGTIKb/U1NPAP//U1P/UFBLAP+HG7n/UVH/VFT/UVH/UVH/U1P/UVH/U1P/UVH/U1P/UlL/UVH/U1NNAP//UVH/UVH/UVFNAP//UlL/UlL/UlL/UlJLAP//UlL/UlL/U1MTAD5KGBheHx9HFhZGFhZFFhb/UlJMGRk+ExNNGBg8ExP/UlL/UlJAFBT/U1P/UlL/U1P/UlL/UlL/UlL/UlLZRkb/UlL/UlL/UlL/UlJDAOLiSUn/UlL/UlJEAOf/U1NGAO3/UlL/UVFHAPH/UlL/UlLxTU1MAP//UlIAAABMAP//UlL/UlJMAP8AAAD/UlL/UlIAAABMAP/9UVH+UlL/UlL///8T+Es2AAAAZXRSTlMAAQICAwUHCQsMEREWGhoeICQlJigoKiswM0JCRkhVVlhiZWlqd3h7h4qNj5OcoqWprK+2wMDAwcLDxMXIyMnKy8zMzc/T1tfd4uLk5ebo6Onq6+7v7/Hz8/T19vf5+fn6+/z8/hoS1SAAAAABYktHRGolYpUOAAABQElEQVRYw+3Wx1YCQRBG4TJjxBwxY8CAOWfBnBXMCqI1Wu//Am5cyDQ9Pe2/cTF339+qTlUTKU1kRNPD5VZ8sJEMVYuhRLTCE6gTY2fREgwQWW0AAbmJgIC894GAZLtBQNJNICDJMhCQIRS4rwEBiaFAOgQC0o8CcyjwXAkC0kXFrR35dR65e/QAhmnacXXO7nKLemCK3swA84J+MZDjB+A1HXDsE+Al3Sj5BXhZsxV8A7zyBQK8Xki4tQB4p4BwagPw5qcCbFsBvKEAs3ZATpnqUTuAL9xADwqEQeCAQGAMBdpBYJdAoBcE9kpBIEIYMEkYsB/CgKuff9ZfgZM2goBEPSFANlZOWiBlBDLxll+3VAGc+RcP4ONwZiD/Y+N4dJdydd1cpFxzx6paCoAACIB/CzxZAVUqMGIhvI6r778B8fsX3rztq9YAAAAASUVORK5CYII=",
        "mediaType": "image/png"
    },
    "screenshots": [],
    "extensions": [
        {
            "name": "My Connected Fields Extension",
            "description": "Used to verify and autofill agreements with custom data models",
            "template": "ConnectedFields.Version1.ConnectedFields",
            "actionReferences": [
                "My Verify Action",
                "My GetTypeNames Action",
                "My GetTypeDefinitions Action"
            ]
        }
    ],
    "actions": [
        {
            "name": "My Verify Action",
            "description": "This is a description of my verify action",
            "template": "ConnectedFields.Version1.Verify",
            "connectionsReference": "authentication",
            "params": {
                "uri": "<PROXY_BASE_URL>/api/connectedfields/verify"
            }
        },
        {
            "name": "My GetTypeNames Action",
            "description": "This is a description of my GetTypeNames action",
            "template": "DataIO.Version6.GetTypeNames",
            "connectionsReference": "authentication",
            "params": {
                "uri": "<PROXY_BASE_URL>/api/connectedfields/getTypeNames"
            }
        },
        {
            "name": "My GetTypeDefinitions Action",
            "description": "This is a description of my GetTypeDefinitions action",
            "template": "DataIO.Version6.GetTypeDefinitions",
            "connectionsReference": "authentication",
            "params": {
                "uri": "<PROXY_BASE_URL>/api/connectedfields/getTypeDefinitions"
            }
        }
    ],
    "publicationRegions": [
        "US"
    ],
    "distribution": "PUBLIC"
}
```

To use an extension app reference implementation, clone the project files from GitHub and follow the step-by-step instructions provided in the README file located in the root folder of each implementation. These instructions will guide you through setting up either a cloud-based or local environment, including configuring your development tools, running the app, setting up a public endpoint, and preparing the example manifest. The README also includes detailed instructions on how to upload an extension app manifest to the Docusign [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/) to start testing the connection and extensions, as shown below.

To further support developers, we offer instructional videos that walk through the process of setting up a reference implementation and demonstrate how to test an extension app in the Docusign Developer Console and within a Docusign workflow. Currently available are the videos for setting up and testing a [Data Verification](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/bank-account-owner-verification/) or [Data IO](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/data-io/) extension app using the appropriate reference implementation.

Videos:

- [How to Set Up a Reference Implementation for Docusign Extension Apps opens in a new tab](https://youtu.be/_4p7GWK5aoA?list=PLXpRTgmbu4oqnHn6pusz4riseJHKZ42HW)
- [Configuring a Docusign Template to Use a Data Verification Extension App opens in a new tab](https://www.youtube.com/watch?v=0lQEq3DkFyU)
- [Testing a Data Verification Extension App opens in a new tab](https://www.youtube.com/watch?v=oetMhjgtzw8)
- [Setting up a Maestro Workflow to Test a Data IO Extension App opens in a new tab](https://www.youtube.com/watch?v=rIHlS5ZnkuY)
- [Testing a Data IO Extension App opens in a new tab](https://www.youtube.com/watch?v=xwPMUwaZQnA)

Start building with our extension app reference implementations today, and unlock the potential to customize Docusign workflows to meet your unique business needs!

Jumpstart your extension app journey by:

- Signing up for a [free developer account](https://www.docusign.com/developers/sandbox) to get started
- Learning more about [extensions apps](https://developers.docusign.com/extension-apps/) and how to [build them](https://developers.docusign.com/extension-apps/build-an-extension-app/)
- Joining the [Docusign Developer Community](https://community.docusign.com/developer-59?_gl=1*1p82xw4*_gcl_au*NjA5NTA2OTkxLjE3Mjk3MDE1MzI.) for any development support

## Additional resources

- [Docusign Developer Center](https://developers.docusign.com/)
- [Docusign Developers Community](https://community.docusign.com/developer-59)
- [@DocusignDevs on X opens in a new tab](https://x.com/DocusignDevs)
- [Docusign for Developers on LinkedIn opens in a new tab](https://www.linkedin.com/showcase/docusigndevs/)
- [Docusign for Developers on YouTube opens in a new tab](https://www.youtube.com/@DocusignDevs)
- [Docusign Developer Newsletter](https://developers.docusign.com/newsletter/#newsletter-signup)

![Author Karissa Jacobsen](https://images.ctfassets.net/9pvazpst9iwl/56GSAsknmGi0EtIB92ylgp/8175ea8eb46c4f2ba06d9d41b6d3d7b1/Karissa_Jacobsen?fm=avif&q=90&w=500)

Karissa JacobsenDeveloper Advocate

Karissa has been working for Docusign since 2020. As a member of the Developer Advocacy team, she creates content, media and code to help developers learn how to use Docusign technology, represents Docusign at virtual and in-person events, and supports developers on Docusign community forums.

[More posts from this author](https://www.docusign.com/blog/author/karissa-jacobsen)

Share

[Share to LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Ffast-track-your-extension-apps-with-reference-implementations "Share to LinkedIn")[Share to Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Ffast-track-your-extension-apps-with-reference-implementations "Share to Facebook")[Share to X](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.docusign.com%2Fblog%2Fdevelopers%2Ffast-track-your-extension-apps-with-reference-implementations&text=Fast-track your extension apps with reference implementations&hashtags=Docusign "Share to X")

Related posts

- [Developer Support Articles](https://www.docusign.com/blog/developers/developer-support-articles)Published Nov 6, 2025

  [## From the Trenches: Updating document attributes with the CLM API](https://www.docusign.com/blog/developers/from-the-trenches-updating-document-attributes-with-the-clm-api)

  ![Author Guilherme Flores](https://images.ctfassets.net/9pvazpst9iwl/2noNDcPqT2mGSswubBQwpt/2d4e4478faad91c267bdb14ad8dcf013/GuilhermeFlores.jpg?fm=avif&q=90&w=500)

  Guilherme Flores

  [![](https://images.ctfassets.net/9pvazpst9iwl/561nlNdMF62S4LywGbKNCM/440572f961e19c1ed3abcf1745f79e37/GettyImages-1409307140.jpg?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/from-the-trenches-updating-document-attributes-with-the-clm-api)
- [Developers](https://www.docusign.com/blog/developers)Published Aug 15, 2025

  [## Select the right tab placement strategy for your Docusign integration](https://www.docusign.com/blog/developers/select-the-right-tab-placement-strategy-for-your-docusign-integration)

  ![Author Marty Scholes](https://images.ctfassets.net/9pvazpst9iwl/38zvFrrTUxCUDR52s5dOrL/444d305b7a84360903f5517ec364d6bd/Marty_Scholes?fm=avif&q=90&w=500)

  Marty Scholes

  [![](https://images.ctfassets.net/9pvazpst9iwl/6BtcUgvP9lQJBE08wsAudp/86b054b14b373b5216318892fcceeb27/illustration-isometric_cube-movement_inkwell.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/select-the-right-tab-placement-strategy-for-your-docusign-integration)
- [Developers](https://www.docusign.com/blog/developers)Published Jul 31, 2025

  [## Automating File Export to Cloud Storage with Docusign Workflow Builder](https://www.docusign.com/blog/developers/automating-file-export-to-cloud-storage)

  ![Author Julie Gordon](https://images.ctfassets.net/9pvazpst9iwl/6pWetjZY1gCV6eGt1gtX4J/66fc155e0053c16de36ebc64a6baf9c2/JGordonNewPhoto400x400.jpeg?fm=avif&q=90&w=500)

  Julie Gordon

  [![](https://images.ctfassets.net/9pvazpst9iwl/7VhFDaYX9QKhjQApsFAvM/cb8700eaf414ca2b1889aac78afdd2fc/Automate_Workflow_-_Dark_Theme.jpg?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/automating-file-export-to-cloud-storage)

[Developer Support Articles](https://www.docusign.com/blog/developers/developer-support-articles)Published Nov 6, 2025

[## From the Trenches: Updating document attributes with the CLM API](https://www.docusign.com/blog/developers/from-the-trenches-updating-document-attributes-with-the-clm-api)

![Author Guilherme Flores](https://images.ctfassets.net/9pvazpst9iwl/2noNDcPqT2mGSswubBQwpt/2d4e4478faad91c267bdb14ad8dcf013/GuilhermeFlores.jpg?fm=avif&q=90&w=500)

Guilherme Flores

[![](https://images.ctfassets.net/9pvazpst9iwl/561nlNdMF62S4LywGbKNCM/440572f961e19c1ed3abcf1745f79e37/GettyImages-1409307140.jpg?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/from-the-trenches-updating-document-attributes-with-the-clm-api)

[Developers](https://www.docusign.com/blog/developers)Published Aug 15, 2025

[## Select the right tab placement strategy for your Docusign integration](https://www.docusign.com/blog/developers/select-the-right-tab-placement-strategy-for-your-docusign-integration)

![Author Marty Scholes](https://images.ctfassets.net/9pvazpst9iwl/38zvFrrTUxCUDR52s5dOrL/444d305b7a84360903f5517ec364d6bd/Marty_Scholes?fm=avif&q=90&w=500)

Marty Scholes

[![](https://images.ctfassets.net/9pvazpst9iwl/6BtcUgvP9lQJBE08wsAudp/86b054b14b373b5216318892fcceeb27/illustration-isometric_cube-movement_inkwell.png?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/select-the-right-tab-placement-strategy-for-your-docusign-integration)

[Developers](https://www.docusign.com/blog/developers)Published Jul 31, 2025

[## Automating File Export to Cloud Storage with Docusign Workflow Builder](https://www.docusign.com/blog/developers/automating-file-export-to-cloud-storage)

![Author Julie Gordon](https://images.ctfassets.net/9pvazpst9iwl/6pWetjZY1gCV6eGt1gtX4J/66fc155e0053c16de36ebc64a6baf9c2/JGordonNewPhoto400x400.jpeg?fm=avif&q=90&w=500)

Julie Gordon

[![](https://images.ctfassets.net/9pvazpst9iwl/7VhFDaYX9QKhjQApsFAvM/cb8700eaf414ca2b1889aac78afdd2fc/Automate_Workflow_-_Dark_Theme.jpg?fm=avif&q=90&w=500)](https://www.docusign.com/blog/developers/automating-file-export-to-cloud-storage)

## Docusign IAM is the agreement platform your business needs

[Start for Free](https://trial.docusign.com)[Explore Docusign IAM](https://www.docusign.com/intelligent-agreement-management)

![Person smiling while presenting](https://images.ctfassets.net/9pvazpst9iwl/1gOiICnusnBqWxB11vmsFs/99a7ee68a05fa07fe6e5e35186e45394/smiling-woman-in-bright-sweater-presents-charts-on-laptop.png?fm=avif&q=90&w=500)
