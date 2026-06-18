---
title: Set up your test environment
source_url: https://developers.docusign.com/docs/agreement-manager-api/set-up-test-environment/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- Agreement Manager API
- Agreement Manager API
- Set Up Test Environment
scraped_at: '2026-06-18T14:17:04Z'
---

# Set up your test environment

This procedure enables you to set up the Agreement Manager API Postman collection and start testing API requests.

## Prerequisites

To use the Postman collection, you need the following:

- Your Docusign developer account credentials
- A [Postman account](https://www.postman.com/postman-account/)

## One-time setup procedures

In addition to the prerequisites, you’ll need to complete these steps:

- [Create an integration in your Docusign developer account](https://developers.docusign.com/docs/agreement-manager-api/set-up-test-environment/#create-integration-in-docusign-developer-account)
- [Add agreements in Agreement Manager](https://developers.docusign.com/docs/agreement-manager-api/set-up-test-environment/#add-agreements-in-agreement-manager) (optional)
- [Fork the Postman collection and set environment variables](https://developers.docusign.com/docs/agreement-manager-api/set-up-test-environment/#fork-the-postman-collection-and-set-environment-variables)

After you've completed the one-time setup, follow the steps in [Authenticate and execute Agreement Manager API requests](https://developers.docusign.com/docs/agreement-manager-api/set-up-test-environment/#authenticate-and-execute-agreement-manager-api-requests) whenever you want to test Agreement Manager API requests.

### Create integration in Docusign developer account

To authenticate with Docusign so that you can send Agreement Manager API requests, you need to create an integration in your developer account and configure it with the required parameters. This is a one-time setup procedure.

To create the integration:

1. Access the [Apps and Keys](https://admindemo.docusign.com/authenticate?goTo=appsAndKeys) page and supply your Docusign developer account credentials.
2. Select **Add App and Integration Key**.
3. Supply an app name and select **Create App**.
4. Locate the integration key and copy it to a file. You'll need this value later.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='416' width='819' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Integration key](https://images.ctfassets.net/aj9z008chlq0/6EF8wCp0cY44Y8yKj29gHa/05bebda72b0bbf7526d23ed600ca2f05/IntegrationKey.png?w=819&h=416&q=50&fm=png)
5. In the **Authentication** section, select **Add Secret Key** and then copy the generated value to a file. You'll need this value later.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='652' width='836' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Secret key](https://images.ctfassets.net/aj9z008chlq0/4vmYfdAmnvd6tOOq7ksKDr/d06e32f773ff7ae7e8f0f9a8c78f9527/SecretKey.png?w=836&h=652&q=50&fm=png)
6. In the **Additional Settings** section, select **Add URI** and add this URI: https://oauth.pstmn.io/v1/browser-callback

   **Note:** If you plan to test Agreement Manager API requests with your own app instead of Postman, enter a redirect URI to your app.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='206' width='812' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Redirect URI](https://images.ctfassets.net/aj9z008chlq0/6KUCqJGxjmNj9VOVthMpCd/45c99db3692ecd4333fc07234af4a3b8/RedirectURI.png?w=812&h=206&q=50&fm=png)
7. At the bottom of the page, select **Save**.

### Add agreements in Agreement Manager (optional)

In this step, you use the Agreement Manager UI to add sample agreements to your Docusign developer account. Once Agreement Manager has completed AI extraction on the uploaded documents, you'll be able to retrieve the agreement details using Agreement Manager API requests. This is a one-time setup procedure.

Follow the instructions in [Docusign Agreement Manager: Free Trial Sample Agreements](https://support.docusign.com/s/document-item?language=en_US&bundleId=grn1724866350175&topicId=amt1724866817262.html) to download Docusign-provided sample agreements and add them to your Docusign developer account.

You can also upload your own sample agreements. You can upload a maximum of 100 agreements to your account.

### Fork the Postman collection and set environment variables

This procedure enables you to fork the Docusign-provided Agreement Manager (previously called Navigator) API collection into your workspace and configure the forked collection with environment variables required for authentication. This is a one-time setup procedure.

To fork the collection and set environment variables:

1. Access the Docusign API: Limited availability APIs Postman workspace via the link that was sent to you when you were accepted to the LA release.
2. Provide your Postman account credentials.
3. Select **Collections** in the Postman left navigation.
4. In the list of collections, select **Navigator API [version]-beta #examples**.
5. Select the ellipsis to the right of **Navigator API [version]-beta #examples**, and select **Create a fork**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='566' width='582' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Create fork](https://images.ctfassets.net/aj9z008chlq0/5PU9UyJB76B8Hh0pCdTqI7/3f056183a5971dcfc8c6bdd8f377670f/CreateFork.png?w=582&h=566&q=50&fm=png)
6. Enter a **Fork label** and select your workspace or your team's workspace. Docusign recommends leaving **Watch original collection** selected so that you'll be notified of any updates.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='570' width='485' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Fork label and workspace](https://images.ctfassets.net/aj9z008chlq0/2uhgYNVqX5e9hOeVT0UD2X/10e8a030a161881f5ed3453130819b8d/ForkLabelWorkspace.png?w=485&h=570&q=50&fm=png)
7. Select **Fork Collection**.
8. In the **Workspaces** menu, select your workspace to switch to it from the Docusign workspace.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='312' width='637' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Switch workspace](https://images.ctfassets.net/aj9z008chlq0/3wkbmR0JtPxEcxSrCrP6BD/65df17a944251911790458b0a0e4d3f9/SwitchWorkspace.png?w=637&h=312&q=50&fm=png)
9. To the right of the workspace name, select **New**, and then select **Environment**.
10. Select the ellipsis next to the new environment, select **Rename**, and then supply a name for the environment.

    ![](data:image/svg+xml;charset=utf-8,%3Csvg height='278' width='783' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

    ![Rename environment](https://images.ctfassets.net/aj9z008chlq0/33gWtKOO4cP69vwt5T8EXG/8afbeb65a8dd1cd3a001d977357d746a/RenameEnvironment.png?w=783&h=278&q=50&fm=png)
11. Add these variables with values you obtained when you completed the [Create integration in Docusign developer account](https://developers.docusign.com/docs/agreement-manager-api/set-up-test-environment/#create-integration-in-docusign-developer-account) procedure.

    | Variable | Initial and Current Value |
    | --- | --- |
    | `clientId` | The integration key from the integration you created in your Docusign developer account |
    | `clientSec` | The client secret from the integration you created in your Docusign developer account |

    The list will look similar to this:

    ![](data:image/svg+xml;charset=utf-8,%3Csvg height='329' width='1531' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

    ![Environment variables](https://images.ctfassets.net/aj9z008chlq0/3hRAPVHoGgijWdQuQlyUsX/04df081fb904ced5d42d34f77e51adcd/EnvironmentVariables.png?w=1531&h=329&q=50&fm=png)
12. Select **Save**.

## Authenticate and execute Agreement Manager API requests

Once you've completed all the [one-time setup](https://developers.docusign.com/docs/agreement-manager-api/set-up-test-environment/#one-time-setup-procedures) procedures in the previous sections, follow this procedure any time you want to test Agreement Manager API requests.

To authenticate and execute Agreement Manager API requests:

1. Access your Postman workspace.
2. Select **Collections** in the Postman left navigation.
3. In the **Collections** list, select the forked Agreement Manager or Navigator API collection that you created in the previous procedure.
4. In the environment list in the upper right corner, select the environment you created in the previous procedure.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='304' width='500' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Select environment](https://images.ctfassets.net/aj9z008chlq0/4VT5qVSjYABJnkjWBOzb0U/7ccac94c8009a7fbb54e5731c5303c5c/SelectEnvironment.png?w=500&h=304&q=50&fm=png)
5. Make sure that the environment name appears selected.
6. Switch to the **Authorization** tab.
7. Scroll to the bottom and select **Get New Access Token**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='709' width='833' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Authorization tab](https://images.ctfassets.net/aj9z008chlq0/7CipDOC3IM9SS1lFZHkCiI/c2a811af8e42e163d9c77e9bcaa978bf/AuthorizationTab.png?w=833&h=709&q=50&fm=png)
8. On the **Log in to Docusign** window, supply your developer account email, click **Next**, supply your password, and click **Next**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='515' width='678' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Access token login](https://images.ctfassets.net/aj9z008chlq0/5meJjbrgL4VxbAUavKaJ7k/4051ba72ff8ed84325c4f57a80a14cc4/AccessTokenLogin.png?w=678&h=515&q=50&fm=png)

   **Note:** If the window displays the message **The redirect URI is not registered properly with Docusign**, follow the steps in [Create integration in Docusign developer account](https://developers.docusign.com/docs/agreement-manager-api/set-up-test-environment/#create-integration-in-docusign-developer-account) to add the required URI to your integration and save it. Then try the authentication steps again.
9. An **Authentication Complete** window appears, followed by a **Manage Access Tokens** window. Select **Use Token**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='459' width='1247' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Manage access tokens](https://images.ctfassets.net/aj9z008chlq0/5P1E4W6BjyqKW1WuCqnWM5/ae607a3b431268df5facb0b8f5b7d8fd/ManageAccessTokens.png?w=1247&h=459&q=50&fm=png)
10. In the **Collections** list, under your forked collection, expand the **Auth** folder.
11. Select the **User Account Info** request.

    ![](data:image/svg+xml;charset=utf-8,%3Csvg height='129' width='487' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

    ![Get user account info](https://images.ctfassets.net/aj9z008chlq0/1faUt1SMfOq3lOCFehN2Ej/7b4fab1319c069a302332c081c4f2e0e/GetUserAccountInfo.png?w=487&h=129&q=50&fm=png)
12. Select **Send**. The request is executed and a post-request script will populate the account ID associated with your default account as the `accountId` environment variable. If you want to use an ID of another account, replace the value of `accountId` with the preferred value.

You can now execute the [Agreements:getAgreement](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreement/) and [Agreements:getAgreementsList](https://developers.docusign.com/docs/agreement-manager-api/reference/agreementmanager/agreements/getagreementslist/) requests in the **Agreements** folder. They will return the sample agreement data in your account.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='213' width='470' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![GET requests](https://images.ctfassets.net/aj9z008chlq0/1hKEesfmDJBM1nKTUY1CE4/367252714617ad1540d5ec9f39d4048d/GetRequests.png?w=470&h=213&q=50&fm=png)

## Submit feedback or request assistance

You can submit feedback about the Agreement Manager API directly in Postman. Docusign is specifically interested in:

- Feedback about how the API does or does not meet the needs of your organization's use cases
- Ideas for features that would make the API more useful to your organization
- Bug reports. Please provide as much detail as possible, including sample requests and responses where appropriate.

You can also submit questions or support requests directly in Postman.

To submit feedback, questions, or support requests:

1. Select the comment icon in the Postman right navigation menu.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='323' width='450' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Comment icon](https://images.ctfassets.net/aj9z008chlq0/6PCpPs7Nkw22o7cfQAbdg/76bda6a8d7ebe08b4df1984086907651/CommentIcon.png?w=450&h=323&q=50&fm=png)
2. Enter your feedback and select **Comment**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='217.99999999999997' width='486' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Test comment](https://images.ctfassets.net/aj9z008chlq0/5AHpPI0z4EVS6Tv9zteERw/05307c3f90cc8f7abece25b9367198a5/TestComment.png?w=486&h=218&q=50&fm=png)
3. When Docusign responds, you'll receive notification at the email address associated with your Postman account.

## Next steps

- Review [Agreement Manager API use cases](https://developers.docusign.com/docs/agreement-manager-api/concepts/use-cases/).
- See the [API Reference](https://developers.docusign.com/docs/agreement-manager-api/reference/) for details about request and response format.

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
