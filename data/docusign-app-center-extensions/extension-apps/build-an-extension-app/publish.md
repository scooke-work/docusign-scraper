---
title: Publish an extension app to the Docusign App Center
source_url: https://developers.docusign.com/extension-apps/build-an-extension-app/publish/
site: developers.docusign.com
breadcrumb:
- Extension Apps
- Extension Apps
- Build An Extension App
- Build An Extension App
- Publish
scraped_at: '2026-06-18T19:51:50Z'
---

# Publish an extension app to the Docusign App Center

When you add a new extension app to the [Developer Console](https://developers.docusign.com/extension-apps/developer-console-overview/), it is only available in your [developer account](https://developers.docusign.com/platform/account/). This means that only the users in your developer account can see it and use it in the demo environment. If you want to make your extension app available in production and share it with Docusign customers, you can [become a Docusign partner](https://partners.docusign.com/s/join-now) and publish your extension app to the [Docusign App Center](https://apps-d.docusign.com/app-center).

Your extension app must comply with all [publishing guidelines](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/guidelines/) before it can be published, and it must pass a review process. If Docusign approves your extension app and you are a Docusign partner, you can publish it to the App Center where Docusign customers can install it and use it with their own Docusign account. If you choose to build a [private extension app](https://developers.docusign.com/extension-apps/extension-apps-101/choosing-private-distribution/) , you will also have to share it with specific production accounts to make it available to customers.
If you want to build applications for streamlining how millions of customers manage their agreements, publishing them to the App Center is a useful method to distribute your extension app to a large audience of Docusign users.

Once you publish your extension app to the App Center, you cannot unpublish or delete it.

## Steps to publish your extension apps

This guide shows how to publish an extension app to the Docusign App Center, both for public and private extension apps. Where applicable, we’ll state the differences between public and private apps.

**Note:** In the Developer Console screenshots in this procedure, we show the **Distribution** as **Public**, but if you are registering a private extension app, you’ll see your **Distribution** listed as **Private**, as shown here.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='114' width='374' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Extension app listing information](https://images.ctfassets.net/aj9z008chlq0/tfhuxodYRY03umkYxRrA4/3d0e397463d66bfe7dd80ce7853832ae/AppWithPrivateDistribution.png?w=374&h=114&q=50&fm=png)

### Step 1. Have your app ready to be published

To publish an extension app to the Docusign App Center, your app must comply with the [App Center publishing guidelines](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/guidelines/). Please follow the guidelines to ensure that your extension app can pass the review process. Your app must be fully functioning and be tested thoroughly before you can publish it to the Docusign App Center.

### Step 2. Review your extension app listing information

The listing for your extension app in the Docusign App Center is created from the information supplied when you [registered](https://developers.docusign.com/extension-apps/build-an-extension-app/register/) the extension app. You should review the extension app listing details to ensure that you have the information that you expect to see in the App Center. You can review and update this information using either of these two methods:

- [Use a form-based UI](https://developers.docusign.com/extension-apps/build-an-extension-app/register/use-form/app-center-listing/)
- [Use the extension app manifest file](https://developers.docusign.com/extension-apps/build-an-extension-app/update-registration/use-manifest/). For a complete listing of all fields in the app manifest that impact your App Center listing, please check the [app manifest reference](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/).

To see how your extension app listing will appear in the App Center, use the [App Center preview](https://developers.docusign.com/extension-apps/build-an-extension-app/test/app-center-preview/) feature in the Developer Console.

### Step 3. Submit your extension app for review on the Developer Console

Before your app can be published, you must submit it for review by Docusign. To submit your app for review:

1. Log in to the [Developer Console](https://devconsole.docusign.com).

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='669' width='1359' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![My Extension Apps page](https://images.ctfassets.net/aj9z008chlq0/3QwEzGsTCTzPteVDhZLyRn/591aa2a4485fa87e7d3d47307c4fd9c6/DevConsole1.png?w=1359&h=669&q=50&fm=png)
2. On the **My Apps** screen, select the extension app you wish to publish.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Extension app detail page](https://images.ctfassets.net/aj9z008chlq0/5QlkzoLCkJf5wSxEQyeoeY/bc2498560cfbd5b31ec7f926e9eba3c1/DevConsole2.png?w=1603&h=911&q=50&fm=png)
3. Select **Publish to App Center** from the left menu. 

   If your extension app was never published, its app status will be **Draft**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Publish to App Center page](https://images.ctfassets.net/aj9z008chlq0/79duwtbwcdyEkYBcESfmHn/7abf5f006a21dbc0400379c85bcbfdee/DevConsole3.png?w=1603&h=911&q=50&fm=png)
4. Select the **Submit** button to submit your app for review.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![App Submission page](https://images.ctfassets.net/aj9z008chlq0/7DeI2XizTu3A0bV5Fgjsyv/81cab8df3b9b86d7c73bf0d286e4de35/DevConsole4.png?w=1603&h=911&q=50&fm=png)
5. On the web form that opens, supply information that will help the app review team when evaluating your extension app. Not all of these fields are required, but completing every field will help Docusign quickly evaluate your application. The form includes the following fields:
   1. **Submitter name and Submitter email:** The name and email address used to log in to the Developer Console will automatically be populated into the form. You may modify them if you want to use different information.
   2. **Additional contacts:** Optionally, you can provide additional emails (comma-separated) as needed. Docusign will use these email addresses to communicate with you about the status of your submission.
   3. **Test credentials.** A set of credentials (typically username and password) needed for the extension app review team to test your extension app. These credentials (for your own service or services, not Docusign credentials) should be for a test-only account that you set up for this purpose. Do not give your own private credentials or use passwords that you also use for other purposes. The information is stored securely in Docusign and will be removed from our records when the extension app is published. (It is a best practice for you to change this password at that point or remove this account.)
   4. **Test instructions**. Optional information that you want to provide the Docusign app review team before they start testing your extension app; for example, for a data validation extension, how the review team can trigger and verify that invalid form entries are correctly flagged before submission. You can also list minor issues that your development team has yet to fix.
   5. **App name.** App unique identifier. This GUID is used to identify this particular version of your app. **Do not modify this field.**
   6. **App identifier.** App version identifier. This GUID is used to identify this particular version of your app. **Do not modify this field.**
   7. **Region Selected.** This is the list of one or more regions where your app will be published. The list comes from the regions you selected when you [registered](https://developers.docusign.com/extension-apps/build-an-extension-app/register/) the extension app. **Do not modify this field.** See [Globalization](https://developers.docusign.com/extension-apps/extension-apps-101/globalization/) for details about regional availability.
   8. **Additional details.** Optional field for any other relevant information that you want to provide to the app review team to help them with this process.
6. Select **Next** to continue to the signing screen. The signing screen now includes all your app’s information.
7. Select **Submit** to finish the app submission for approval.

After you submit the app, its app status changes to **In Review**. It may take a few days for the Docusign app review team to finish reviewing your submission.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![App has been submitted for review](https://images.ctfassets.net/aj9z008chlq0/6uhlpNhjTc4WpKssH78eS8/05e1628bc8ec08825a9e243429d5008e/DevConsole5.png?w=1603&h=911&q=50&fm=png)

You'll receive an email from Docusign to let you know that your extension app was successfully submitted for review. Look for an email titled **Your Docusign extension app is under review** in your mailbox (or check your spam folder if you can’t find that email message). 

While waiting for Docusign to review your extension app, you may not modify or delete it unless you cancel the review process. To cancel the review, go to the **Publish to App Center** page of the relevant app, and select **Cancel Review**. This will set your app status back to **Draft** and will enable you to edit and resubmit it for review later.

Note that only Docusign partners may publish public extension apps. Docusign will verify your status as a partner during this review process. If you are not currently a partner, Docusign will contact you to discuss becoming a partner, and your app will stay in an In-Review status until onboarding is complete. Your app must still pass the full review process. See [Join now](https://partners.docusign.com/s/join-now) for details on how to join the Docusign partner program.

### Step 4. Publish your approved extension app

When the Docusign app review team approves your extension app, you will receive another email titled **Your extension app has been approved**. In the Developer Console, your extension app status will change from **In Review** to **Approved**.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Extension app has passed review](https://images.ctfassets.net/aj9z008chlq0/1G8mqTdqTEiNNZbzpxKU0g/12c0bb8daaf6a33a33524f26ada05d2a/DevConsole6.png?w=1603&h=911&q=50&fm=png)

Please note that your extension app is not yet published and therefore is not yet available in the App Center for users (except users in your developer account). You can choose to cancel and not publish your app if you still want to modify it before you publish it. If you choose the **Cancel** button and confirm you wish to cancel, you’ll have to submit your app for review again before it can be published. To publish your extension app to the App Center:

1. Find your extension app in the Developer Console and select **Publish to App Center.**
2. Select the **Publish** button that becomes available after Docusign has approved your extension app.

At this point the app status will change from **Approved** to **Live**. If this is a public extension app, it will immediately be available in the App Center for all Docusign customers in the [regions](https://developers.docusign.com/extension-apps/extension-app-reference/app-manifest-reference/) you selected. If this is a private extension app, it will still have to be shared with selected production accounts for it to be available for customers; see Step 5B for details on this process.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Extension app after publication](https://images.ctfassets.net/aj9z008chlq0/TVUsdfzMauJJuJfptub2a/143d7153aaca6597c7b949534c155aa1/DevConsole7.png?w=1603&h=911&q=50&fm=png)

**Note:** Once published, a public extension app cannot be removed from the Developer Console or from the App Center. If you do need to remove it, please visit the [Docusign Developer Community](https://community.docusign.com/developer-59) for information and assistance.

### Step 5A. Public extension apps: Check out your extension app in the Docusign App Center

Congratulations! Your extension app is live and can be installed by Docusign customers from the Docusign App Center. It’s time to celebrate and think about how to promote your extension app to ensure its success.

![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

![Public extension apps listed in the App Center](https://images.ctfassets.net/aj9z008chlq0/1liKmXciypBCGx2XGjFL1J/d0a6cf881bf23b908fca985f236b1585/AppCenter0.png?w=1603&h=911&q=50&fm=png)

### Step 5B. Private extension apps: Share your extension app

Private distribution is currently in beta.

After completing steps 1-4 for private extension apps, you are now ready to share your private extension app with selected production customers. This step is not optional. While your app is now live, it is not yet available to any production customer. To make private extension apps visible and usable to production customers, you must provide their **ACCOUNT ID**. An account ID is a unique identifier (GUID) for any Docusign account. In order to find an account ID, a customer can go to their [Apps and Keys](https://admin.docusign.com/authenticate?goTo=apiIntegratorKey) page and copy their **API Account ID** value. Note that we only support production accounts based in the US data centers (NA1, NA2, NA3, and NA4).

1. Follow items 1-3 in Step 3 above to find your extension app and go to the **Publish to App Center** page.
2. Since your private extension app is now live, you’ll see a new section called **Share your private app**.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Share a private extension app](https://images.ctfassets.net/aj9z008chlq0/4Ria3P05ii31W0mdnTd2Fp/d5a2d8462726a5e59085e815d4d12581/DevConsole8.png?w=1603&h=911&q=50&fm=png)
3. Select **+Add** to add an account to the list.
4. In the **ACCOUNT ID** field, enter the production account GUID for the account you wish to add as explained above.
5. The **ALIAS** field is for your own tracking purposes. We recommend you use a name that will help you identify the account you’re using later.
6. Select the checkmark.
7. You will now see the new account ID added to the list with a **PENDING** status.

   ![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

   ![Shared account in pending status](https://images.ctfassets.net/aj9z008chlq0/49NOdxbcFlUqN1QyiCoZxT/4ee7c79c6c0ba5d88c8365a98ca433eb/DevConsole9.png?w=1603&h=911&q=50&fm=png)
8. At this point, the administrator of the production account that you added needs to log in to the [Docusign App Center](https://apps.docusign.com/app-center) (in production) to approve the new extension app for their account.
9. After the administrator selects **Accept** in App Center, they’ll go to the listing for the new extension app (in App Center) and be able to install it for all members of their account.
10. At this point, back in the Developer Console, if you navigate back to the **Publish to App Center** page, you’ll see that the account that you added now shows in **ACCEPTED** status, letting you know the the administrator of the production account has added the app to be available in App Center.

    ![](data:image/svg+xml;charset=utf-8,%3Csvg height='911' width='1603' xmlns='http://www.w3.org/2000/svg' version='1.1'%3E%3C/svg%3E)

    ![Private extension app accepted by account admin](https://images.ctfassets.net/aj9z008chlq0/7eSa3c6DNgVI1h3MGzuTCJ/0b3b75a493e506dcb54d8f17fe9db9a7/DevConsole10.png?w=1603&h=911&q=50&fm=png)

#### Optional: Remove an account from a private extension app

If you need to remove one of the accounts that were previously added to share a private extension app, you can do so at any time. Simply find the account in the list and select the delete icon on the right. It does not matter if the status of the account is **PENDING** or **ACCEPTED**. As soon as you do that, you’ll get a confirmation dialog with this message: **Are you sure you want to remove this account?**

Once you select **Remove**, the app is immediately removed from the account. The administrator of the account is not notified. You should be careful removing an app after it has already been accepted, as it may be in use by customers.

## Developer and production environments

It’s important to understand that the process of publishing extension apps to the App Center includes two different environments. The [developer environment](https://account-d.docusign.com/) is where you do all your work to register and test your extension app. It’s where you start when you use the Developer Console.

When you publish your extension app to the Docusign App Center, it is automatically published in both the developer environment (also known as *demo*) and the [production environment](https://apps.docusign.com/send/home). Customers who want to use your extension app can then install it in the production environment App Center as well as in the [demo environment App Center](https://apps-d.docusign.com/app-center) if they are using that environment. If you have multiple [developer accounts](https://developers.docusign.com/platform/account/), publishing an extension app that you registered in one of those accounts enables you to install the app to your other accounts in the demo environment App Center.
 **Note**: You cannot use your extension app in production unless it was published to the Docusign App Center.

## Next steps

- Review [Extension app best practices](https://developers.docusign.com/extension-apps/best-practices/).
- See [App Center publishing guidelines](https://developers.docusign.com/extension-apps/build-an-extension-app/publish/guidelines/).
- Check [Support resources and FAQs](https://developers.docusign.com/extension-apps/support-faqs/).
- View a [dashboard](https://developers.docusign.com/extension-apps/build-an-extension-app/monitor-usage/) that displays extension app usage data.
- Retrieve [logs](https://developers.docusign.com/extension-apps/troubleshooting/review-logs/) of extension app installations and other activity.

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
