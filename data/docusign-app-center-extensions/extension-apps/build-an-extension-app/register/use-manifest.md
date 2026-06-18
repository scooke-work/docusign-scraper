---
title: Use a manifest file to register an extension app
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-manifest/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Register
- Register
- Use Manifest
scraped_at: '2026-06-18T19:51:50Z'
---

# Use a manifest file to register an extension app

This guide describes the steps for registering an extension app by building a JSON app manifest file. You also have the option of registering an extension app [using a form](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/). See [Form-based and app manifest method comparison](https://developers.docusign.com/extension-apps/build-an-extension-app/register/#form-based-and-app-manifest-method-comparison) for guidance about which method might be more useful.

The example code in this procedure implements a file output to cloud storage [use case](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/).

Before starting this procedure, make sure that you have completed or obtained the items listed in [Prerequisites for registering an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/register/#prerequisites-for-registering-an-extension-app).

## Step 1. Register a new app in the Developer Console

Open the [Developer Console](https://devconsole.docusign.com) and select **Create App**, and then **By editing the manifest** in the upper right corner of the screen.

## Step 2. Create an extension app manifest

The app manifest editor opens, containing an extension app manifest template. This is where you will create or upload the [extension app manifest](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extension-app-manifest/). The app manifest is a JSON file that defines these parameters for an extension app:

- [Connection](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/connections/)
- [Extensions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/extensions-and-extension-points/)
- [Actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/)

  See [What's inside an extension app](https://developers.docusign.com/extension-apps/extension-apps-101/inside-an-extension-app/) for details about how these components function.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='1858' width='2874' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![A screenshot of the JSON editor in the Developer Console](https://images.ctfassets.net/aj9z008chlq0/10iL048qHpwWnEo8odOimJ/065e2448df4842b0253474744ae4cfc5/DevConsolePrivateAppsUpdate.png?w=2874&h=1858&q=50&fm=png)

You can create and edit your manifest directly in the manifest editor, or you can use the buttons in the top right corner of the manifest editor to download or copy the manifest template to edit it in the IDE of your choice. You can also download the manifest template by choosing **Download** under **Download a template** in the left column on the screen shown above. If you edited your manifest in your IDE, save it as a JSON file and upload it, either by dragging and dropping the file in the box on the left of the screen shown above, or by choosing **Select File**. After your manifest has been uploaded, it will replace the manifest template in the app manifest editor. You can continue to make any necessary edits in the manifest editor.

### Extension app information

The properties defined at the beginning of the extension app manifest—the name, short and long descriptions, images, publisher details, and relevant URLs—will appear in the [Docusign App Center](https://developers.docusign.com/extension-apps/extension-apps-101/app-center/) when the extension app is published. Each extension app that you create needs to have a unique name. The `distribution` property determines whether your app will be [public or private](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/). The value of `distribution` cannot be changed once the app is live. You can change the `distribution` value when the app is in **Draft**, **Approved**, or **Rejected** status.

The `publicationRegions` property determines the regions in which the app will be available for production use. Once an app is live, you can add regions, but you cannot remove them. See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for more information.

To add an icon to your extension app, set the value of `icon.data` to the Base64 representation of your image. Set the value of `icon.mediaType` to the [media type](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) of the icon.

To convert an image file to Base64, you can use commands like these:

- Windows (PowerShell): `[Convert]::ToBase64String((Get-Content TestImage.png -Encoding Byte)) >> output.txt`
- UNIX/Linux: `cat TestImage.png | base64 | pbcopy`

A number of Base64 image converter utilities are also available on the internet. Guidelines for icons and screenshots appear in [Extension app best practices](https://developers.docusign.com/extension-apps/best-practices/).

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

{

"name": "File Output Cloud Storage",

"description": {

"short": "This is a sample short description",

"long": "This is a sample long description"

},

"publisher": {

"name": "Fontara",

"email": "sampleemail@fontara.com"

},

"termsOfServiceUrl": "https://www.fontara.com/tos",

"privacyUrl": "https://www.fontara.com/

privacy-security",

"supportUrl": "https://www.fontara.com/support",

"icon": {

"data": "54ba2e...097bf1=",

"mediaType": "image/png"

},

"signupUrl": "https://www.fontara.com/signup",

"changelog": "",

### Connections

The next section of the extension app manifest defines the extension app’s connections. The [connection object](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/connection/) contains all of the data needed to connect with an external API, API proxy, or identity provider. The connection name must be a unique value that will be used again later when defining the extension app’s actions. Within the `connections` object, set these values within the `params` property:

- `clientId` and `clientSecret`: These values should come from the external platform or identity provider.
- `provider`: This value should be set to `CUSTOM`.
- `scopes`: List any scopes that need to be requested during authorization.
- `grantType`: Indicates whether the extension app uses [Authorization Code Grant](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/#authorization-code-grant) (`authorization_code`) or [Client Credentials Grant](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/#client-credentials-grant) (`client_credentials`).
- `customConfig`: The `customConfig` object that will store the following properties related to your extension app’s custom configuration:
  - `tokenUrl` and `authorizationUrl`: Set these values to the endpoints for getting the token and authorization.
  - `authorizationParams`: Use this property to store any query parameters needed for the authorization endpoint.
  - `authorizationMethod`: Set this value to either `header` or `body`.
  - `scopeSeparator`: Set this value to the delimiter that will be used to separate your needed scopes.

**Note**: Docusign automatically generates a `redirect_uri` value based on your provided `authorizationUrl` and passes this value back to you as a query parameter. Do not hard-code the `redirect_uri`. It may contain one of several values, depending on your region and environment. See [Authorization](https://developers.docusign.com/extension-apps/build-an-extension-app/it-infrastructure/authorization/) for details.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

"connections": [

{

"name": "authentication",

"description": "Secure connection to

sample extension app",

"type": "oauth2",

"params": {

"provider": "CUSTOM",

"clientId": "[omitted]",

"clientSecret": "[omitted]",

"scopes": [],

"grantType": "authorization\_code",

"customConfig": {

"authorizationMethod": "header",

"authorizationParams": {

"prompt": "consent",

"access\_type": "offline"

},

"authorizationUrl": "https://www.

fontara.com/api/oauth/authorize",

### Extensions

After defining your extension app’s connections, you can create an `extensions` object to define the group of tasks that your extension app executes and an `actions` object to define each one of those tasks. In the `extensions` object, define the following properties:

- `template`: This value should be set to the unique string identifier that references the predefined [extension contract](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) for your extension provided by Docusign.
- `actionReferences`: List the actions that make up your extension.

  The names in the `actionReferences` object must match the names of actions defined in the `actions` object of your extension app manifest.
- `capabilities`: List the optional capabilities that make up your extension. The names listed here should match the names of actions defined in the actions object of your extension app manifest. Not all extension types currently support capabilities.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

"extensions": [

{

"name": "File Output Cloud Storage",

"description": "Used to store files to

cloud storage",

"template": "FileIO.Version1.

FileOutputCloudStorage",

"actionReferences": [

"write-file",

"list-directory-contents",

"list-drives"

],

"capabilities": [

"FileIO.Version1.

ListDirectoryContents",

"FileIO.Version1.ListDrives"

]

}

],

### Actions

To define the extension's [actions](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/actions/), add them to your extension app manifest in the list of actions. Optional [capabilities](https://developers.docusign.com/extension-apps/extension-apps-101/concepts/capabilities/) can also be added to this list for extensions where capabilities are supported.

- `name` and `description`: These values describe your action and give it a name. The value of `name` will be referenced in the `actionReferences` field in the `extensions` object. For file IO extensions, Docusign predefines the name values. See the [extension contract](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) reference for details. For other extensions, any value can be used.
- `template`: This value defines the contract of the action and should be set to the unique string identifier of the template for the contract. You can access the action contracts for each extension from the [Extension contracts](https://developers.docusign.com/extension-apps/extension-app-reference/extension-contracts/) page.
- `connectionsReference`: This value should match the value of the `name` parameter in the `connections` object in your extension app manifest.
- `params`: Use this parameter to specify the external API endpoint or API proxy endpoint that will be called by the action.

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

"actions": [

{

"name": "write-file",

"description": "This is a description of

my write file action",

"template": "FileIO.Version1.WriteFile",

"connectionsReference": "authentication",

"params": {

"uri": "https://www.fontara.com/api/

writefile"

}

},

{

"name": "list-drives",

"description": "This is a description of

my list drives action",

"template": "FileIO.Version1.ListDrives",

"connectionsReference": "authentication",

"params": {

"uri": "https://www.fontara.com/api/

### Screenshots

Finally, to add screenshots to your extension app, set the value of `screenshots[].data` to the Base64 representation of your images. Set the value of `screenshots[].mediaType` to the media type of the screenshot. You can add up to four screenshots.

This JSON snippet shows how the parameters appear in the extension app manifest.

Once you have set all of those values, your extension app manifest is ready to be uploaded and validated. See the [App manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) for a full list of supported elements.

1

2

3

4

5

6

"screenshots": [

{

"data": "VBERi0...VPRgo=",

"mediaType": "image/png"

}

]

## Step 3. Validate your app manifest

When your app manifest is ready, select **Validate** to determine if your manifest has any errors. See [Troubleshooting manifest errors](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/troubleshooting-manifest-errors/) for a list of possible errors with details on how to troubleshoot them. Once your manifest has passed all validation checks, you can choose **Create App** to finish registering your application.

## Next steps

- Learn how to [Test an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/test/).
- Review [Example extension app use cases](https://developers.docusign.com/extension-apps/build-an-extension-app/example-use-case/).
- [Publish an extension app](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/) on the Docusign App Center.

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
