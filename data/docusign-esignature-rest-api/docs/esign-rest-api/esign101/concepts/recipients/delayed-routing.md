---
title: Delayed routing
source_url: https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/delayed-routing/
site: developers.docusign.com
breadcrumb:
- APIs
- APIs
- eSignature REST API
- eSignature REST API
- API 101
- API 101
- Concepts
- Concepts
- Recipients
- Recipients
- Delayed Routing
scraped_at: '2026-06-18T20:28:19Z'
---

# Delayed routing

eSignature REST API 2.1 only

The *delayed routing* feature enables you to set a delay between steps of an envelope's routing order. The *routing order* defines the sequence in which an envelope is delivered to recipients. If you set a delay for a step in the routing order, the envelope will be placed on hold after all recipients in the previous step complete their required actions, and a delay countdown will begin. When it has elapsed, the envelope will be sent to recipients in the current step of the routing order. You can define the delay as:

- A length of time after the completion of the previous step’s recipient signing process
- An absolute date and time

You can use delayed routing to control the delivery time for recipients at any step in the routing order after the initial send. To set the time for the initial send, use the [scheduled sending](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/scheduled-sending/) feature. Another feature enables you to [pause envelope delivery](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/pause-unpause-workflow/) before sending to recipients at a step in the routing order, but the pause feature differs from delayed routing and scheduled sending by requiring an API call to [resume envelope routing](https://developers.docusign.com/docs/esign-rest-api/how-to/unpause-workflow/). All three options are part of a suite of eSignature platform features known as *Advanced Recipient Routing* (ARR).

**Note:** The delayed routing feature is available in all developer accounts, but only in certain production account plans. Contact [Docusign Support](https://support.docusign.com/s/contactSupport) or your account manager to find out whether delayed routing is available for your production account plan.

## Why delay the routing of an envelope?

By default, completion of the signing process for one step in the routing order causes an envelope to be sent immediately to recipients defined for the next step. However, business needs may require a length of time to elapse before delivery to the next set of recipients. You can set up delayed routing at any step or multiple steps to hold up envelope delivery as needed.

Scenarios in which you can apply delayed routing include:

- You want to delay sending real estate documents to a recipient until the previous signer’s grace period for withdrawing from the deal has expired.
- A recipient needs access to view a document for a length of time before receiving a signable version. You can define the recipient in one step as a carbon copy recipient (with view-only access), while in the next step defining the same recipient as a signer, and add a delay between the two steps.

## Add delayed routing to a workflow

You can add delayed routing to the routing order by defining it in an envelope’s or template’s workflow. To implement delayed routing:

1. When you create an [envelope](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) or [template](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/create/), add a `workflow` object.
2. In the `workflow` object, define one or more `workflowSteps` objects, each of which represents a step in the routing order.
3. To set a delay before an envelope is routed to recipients at a particular step in the routing order, include a `delayedRouting` object in the `workflowSteps` object associated with that step. Several other properties must be defined in the `workflowSteps` object. They are described in [How to send an envelope with delayed routing](https://developers.docusign.com/docs/esign-rest-api/how-to/send-envelope-with-delayed-routing/).
4. In the `delayedRouting` object, include a `rules` array.
5. To define when the envelope will be sent to recipients associated with this step in the routing order, in the `rules` array, add a `rule` object with one of the following properties:
   - `delay`: A delay between the completion of the previous step and the time the envelope is sent to recipients in this step. This value is a string in `[d.]hh:mm:ss` format, defined as:
     - `[d]`: the number of days from 0 to 30, optional
     - `hh`: hours from 00 to 23
     - `mm`: minutes from 00 to 59
     - `ss`: seconds from 00 to 59
   - `resumeDate`: A specific date and time when the envelope should be sent to recipients in this step. This value is an [ISO8601 datetime](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/delayed-routing/#:~:text=value%20is%20an-,ISO8601%20datetime,-string%20with%20the) string with the time zone specified. For example, `2022-04-03T23:30:00Z` represents a send date and time of April 3, 2022 at 11:30 PM UTC. The `resumeDate` option is not available for templates.

For details and example code, see [How to send an envelope with delayed routing](https://developers.docusign.com/docs/esign-rest-api/how-to/send-envelope-with-delayed-routing/).

## Delayed routing with bulk sending

Delayed routing supports bulk sending a batch of envelopes to a list of recipients. The general steps for implementing bulk sending with delayed routing are:

1. Define a bulk list of recipients via a request to [BulkSend:createBulkSendList](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendlist/).
2. Define a draft envelope or a template that will serve as the basis for the bulk send batch envelopes, including workflow that contains a delay, in an [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) or [Templates:create](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/create/) call.
3. Ensure that the bulk list is compatible with the draft envelope or template by making a request to [BulkSend:createBulkSendTestRequest](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendtestrequest/).
4. Correct any issues that the compatibility check finds by updating the [envelope](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/), [template](https://developers.docusign.com/docs/esign-rest-api/reference/templates/templates/update/), or [bulk list](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/updatebulksendlist/).
5. Generate the bulk send batch envelopes and send them to recipients in the bulk list by calling [BulkSend:createBulkSendRequest](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendrequest/).

When a delay has been defined in the workflow, the delay countdown starts and ends independently for each envelope in the batch, once that envelope reaches the step in the routing order that has a delay. For example, if a delay of one day is defined between the first and second step of an envelope’s routing order, and the bulk list consists of two sets of recipients, the batch envelope delays might be processed as follows:

Batch envelope 1

- July 7: Initial send
- July 9: First signer completes envelope and delay starts
- July 10: Delay ends and envelope is sent to second signer

Batch envelope 2

- July 7: Initial send
- July 11: First signer completes envelope and delay starts
- July 12: Delay ends and envelope is sent to second signer

For a walkthrough of the calls to create a bulk send recipient list, apply it to an envelope, and send the batch of envelopes, see [How to bulk send envelopes](https://developers.docusign.com/docs/esign-rest-api/how-to/bulk-send-envelopes/).

## Retrieve, update, and delete delayed routing parameters

The [EnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/) resource defines endpoints that you can use to retrieve, update, and delete delayed routing parameters for envelopes and templates.

## Cancel a delay

If you attempt to delete delayed routing from an envelope once the delay countdown has begun, you’ll receive an error response. To remove a delay while a countdown is in progress, you can send an [EnvelopeWorkflowDefinition:updateEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopedelayedroutingdefinition/) request and set the delay or send time to one minute in the future. This will reset the countdown, and the envelope will proceed to the recipients at this step in the routing order one minute later.

**Note:** Before a delayed routing countdown has begun, you can use the [EnvelopeWorkflowDefinition:deleteEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopedelayedroutingdefinition/) endpoint or the [EnvelopeWorkflowDefinition:deleteTemplateDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplatedelayedroutingdefinition/) endpoint to remove delayed routing. However, the workflow step that included delayed routing will remain, with a `pause_before` action. This will cause the envelope to become paused indefinitely at this stage in the routing order, and a call to [unpause](https://developers.docusign.com/docs/esign-rest-api/how-to/unpause-workflow/) it will be required. To completely remove any delay or pause between recipients in the routing order, you can use the [EnvelopeWorkflowDefinition:deleteEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deleteenvelopeworkflowstepdefinition/) request or [EnvelopeWorkflowDefinition:deleteTemplateWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/deletetemplateworkflowstepdefinition/) request instead, as long as the step doesn’t include any other workflow rules that should remain intact.

## Behaviors and restrictions

Delayed routing has the following behaviors and restrictions:

- If you define delayed routing for a step in the routing order, the delay applies to all recipients associated with that step.
- Delays can be up to 30 days from completion of the previous step in the routing order. This limit applies to both delays and specific send times. When using a specific send time, the 30-day limit applies to the length of time between completion of the previous step and the `resumeDate`.
- The delay countdown begins when all recipients associated with a step in the routing order have completed the signing process. For example, if you set a one-hour delay before an envelope is sent to step 2 recipients, the one-hour countdown starts when the last of the step 1 recipients has completed the signing process.
- In a bulk send scenario, a separate delay countdown occurs for each batch envelope. A countdown begins when all of a batch envelope’s recipients associated with a step in the routing order have completed the signing process.
- If you define a specific send time for delayed routing, and the previous step in the routing order is completed after the send time, the envelope will be sent to the current step’s recipients immediately on completion of the previous step.
- If a recipient declines to sign, the envelope will not be routed to any subsequent recipients in the routing order, and any delays associated with subsequent recipients will be ignored.
- If an envelope expires while it is paused prior to sending to the next recipient, it will not be sent.
- If an envelope includes [conditional recipient routing](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/conditional-recipients/) as well as delayed routing, and the conditions are not met for an envelope to be delivered to a recipient, any delay associated with that recipient will be skipped and recipient routing will proceed to the next step.
- You can [correct an envelope](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/) while it’s in a paused status as a result of delayed routing. You can also modify a delay during the paused state.

## Envelope statuses

Several types of status are updated as an envelope moves through the delayed routing process. To track envelope status during delayed routing, you may need to check all of these status types:

- **[Envelope status](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/status-codes/#envelope-status-code-descriptions)****:** The overall envelope status.
- **Workflow status:** The overall state of the envelope workflow. For more information, see [Envelopes:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/), scroll down to the **Responses** section, and on the **Definitions** tab for a success response, expand the `workflow` object.
- **Workflow step status:** Indicates whether a step is currently being executed. For more information, see [Envelopes:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/), scroll down to the **Responses** section, and on the **Definitions** tab for a success response, expand the `workflowstep` object.
- **Delayed routing status:** Indicates whether the delay countdown for a step in the routing order is in progress. For more information, see [Envelopes:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/), scroll down to the **Responses** section, and on the **Definitions** tab for a success response, expand the `delayedrouting` object.

Workflow and delayed routing statuses are not included in [Connect](https://developers.docusign.com/platform/webhooks/connect/) messages. To determine the current status, you can use the following calls:

- [EnvelopeWorkflowDefinition:getEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopedelayedroutingdefinition/): Returns delayed routing status for a workflow step.
- [EnvelopeWorkflowDefinition:getEnvelopeWorkflowStepDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopeworkflowstepdefinition/): Returns workflow step and delayed routing status for a workflow step.
- [Envelopes:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/): If you specify an `include` query parameter with a value of `workflow`, this call returns the workflow, workflow step, and delayed routing statuses for an envelope, in addition to the envelope status. If you omit the `include` query parameter, this call does not return workflow, workflow step, and delayed routing information.
- [EnvelopeWorkflowDefinition:getEnvelopeWorkflowDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/getenvelopeworkflowdefinition/): Returns the workflow, workflow step, and delayed routing statuses for an envelope.

**Note:** Do not call these methods more than once every 15 minutes. Making excess calls to check envelope status will violate Docusign polling rules and can increase your risk of being locked out for exceeding [API call limits](https://developers.docusign.com/docs/esign-rest-api/esign101/rules-and-limits/).

## Status changes during delayed routing

Docusign applies the following statuses to envelopes at each stage of delayed routing processing.

| Stage | Envelope status | Workflow status | Workflow step status | Delayed routing status |
| --- | --- | --- | --- | --- |
| An envelope has been created as a draft (the `status` in the [Envelopes:create](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/create/) call was `created`). The envelope sending process will not be initiated until a call to [Envelopes:update](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/update/) or [BulkSend:createBulkSendRequest](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/createbulksendrequest/) changes the `status` from `created` to `sent`. | `created` | `pending` | `pending` | `pending` |
| The envelope sending process has been initiated, but the envelope has not reached a step at which a delay has been defined. | `sent` | `pending` | `pending` | `pending` |
| The envelope has reached a step that includes a delay, and the time or delay specified for the envelope to be sent to this step’s recipients has not arrived or elapsed. | `sent` | `paused` | `in_progress` | `started` |
| The time or delay specified for the envelope to be sent to the current step’s recipients has arrived or elapsed, and the envelope has been sent to this step’s recipients. | `sent` | `completed` | `completed` | `completed` |

## Delayed routing status for bulk send batch envelopes

For a delayed routing workflow with a bulk send batch, status changes associated with the start and end of a delay are applied to the batch envelopes, but not to the original draft envelope that served as the basis for the batch envelopes. The original draft envelope remains in a `created` status with a workflow step status and delayed routing status of `pending`. See [BulkSend Resource](https://developers.docusign.com/docs/esign-rest-api/reference/bulkenvelopes/bulksend/) for a list of API calls that return information about batch envelopes and their statuses.

## Delayed routing status change example with two delays

Below is an example of part of a JSON response to an [Envelopes:get](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopes/get/) call that shows the envelope, workflow, workflow step, and delayed routing statuses. In this example, the routing order consists of three steps with delays before sending envelopes to recipients in the second and third steps.

```
{
"status": "sent",
"workflow": {
"resumeDate": "2022-03-03T21:15:04.5872828Z",
"workflowStatus": "paused",
"currentWorkflowStepId": "5e6899dd-xxxx-xxxx-xxxx-3d98645827f9",
"workflowSteps": [
    {
        "action": "pause_before",
        "triggerOnItem": "routing_order",
        "itemId": "2",
        "workflowStepId": "795ee946-xxxx-xxxx-xxxx-19da793518cb",
        "status": "completed",
        "triggeredDate": "2022-03-03T21:04:03.3908285Z",
        "delayedRouting": {
            "status": "completed",
            "resumeDate": "2022-03-03T21:07:03.3596049Z",
            "rules": [
                {
                    "delay": "00:03:00"
                }
            ]
        }
    },
    {
        "action": "pause_before",
        "triggerOnItem": "routing_order",
        "itemId": "3",
        "workflowStepId": "5e6899dd-xxxx-xxxx-xxxx-3d98645827f9",
        "status": "in_progress",
        "triggeredDate": "2022-03-03T21:09:04.6185285Z",
        "delayedRouting": {
            "status": "started",
            "resumeDate": "2022-03-03T21:15:04.5872828Z",
            "rules": [
                {
                    "delay": "00:06:00"
                }
            ]
        }
    }
]
},
```

In a delayed routing scenario consisting of three steps with delays before the second and third steps, the complete list of status changes is:

| **Stage** | **Envelope status** | **Workflow status** | **Step 2 workflow status** | **Step 2 delayed routing status** | **Step 3 workflow status** | **Step 3 delayed routing status** |
| --- | --- | --- | --- | --- | --- | --- |
| Envelope has been sent to step 1 recipients. | `sent` | `pending` | `pending` | `pending` | `pending` | `pending` |
| Step 1 recipients have signed, and the delay countdown for the send to step 2 recipients is in progress. | `sent` | `paused` | `in_progress` | `started` | `pending` | `pending` |
| The delay for step 2 recipients has elapsed and envelopes have been sent to step 2 recipients. | `sent` | `pending` | `completed` | `completed` | `pending` | `pending` |
| Step 2 recipients have signed, and the delay countdown for the send to step 3 recipients is in progress. | `sent` | `paused` | `completed` | `completed` | `in_progress` | `started` |
| The delay for step 3 recipients has elapsed and envelopes have been sent to step 3 recipients. | `sent` | `completed` | `completed` | `completed` | `completed` | `completed` |
| Step 3 recipients have signed. | `completed` | `completed` | `completed` | `completed` | `completed` | `completed` |

## Error codes

Docusign returns the following codes to report errors related to delayed routing. The API returns the upper-case error code and the message text.

| Error code | Message text | Description |
| --- | --- | --- |
| ACCOUNT\_LACKS\_PERMISSIONS | This Account lacks sufficient permissions. | The request workflow contains `delayedRouting` delay rules, but the requesting user's account does not have delayed routing available in their account plan. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. `action` property must be specified. | The request is missing a required `action` property, which specifies the action to take. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. Envelope delay rules supports specifying either a 'resumeDate' or 'delay', but not both. | The `workflowSteps delayedRouting` property contains a `rule` object with a value defined for both the `delay` and `resumeDate` properties. Only one of these properties should be defined. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. Invalid value for 'delay': {delay}. | The `workflowSteps` `delayedRouting` property contains a `rule` object with an invalid value for the `delay` property. The value must be a timespan string in the format `days.hours:minutes:seconds` with these components:  - `days`: an optional integer value up to 30, omitted if less than 1 - `hours`: two digits between 00 and 23 - `minutes`: two digits between 00 and 59 - `seconds`: two digits between 00 and 59 |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. Invalid value for 'delayedRouting.rules', expected rules list to contain at most 1 rule but {rules.Count} rules were defined. | The request workflow contains a `workflowSteps` definition with a `delayedRouting` property whose `rules` array contains more than one `rule` object. Only one `rule` object is permitted. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. Invalid value for 'resumeDate': {resumeDate}. | A `workflowSteps delayedRouting` property contains a `rule` object with an invalid value for the `resumeDate` property. The value must be a properly formatted [ISO8601 datetime](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/delayed-routing/#:~:text=value%20is%20an-,ISO8601%20datetime,-string%20with%20the) string. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. Invalid value for workflow step 'delay', must be a positive value: {step.DelayedRouting.Rules[0].Delay}. | The request workflow has a `workflowSteps` object whose `delayedRouting delay` rule differs from the saved workflow's `delayedRouting delay` rule, and the request `delay` is either zero or a negative timespan. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. Invalid value for workflow step 'resumeDate', must not be in the past: {step.DelayedRouting.Rules[0].ResumeDate}. | The request workflow has a `workflowSteps` object whose `delayedRouting resumeDate` rule differs from the saved workflow's `delayedRouting resumeDate` rule, and the request’s `resumeDate` is in the past. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. `itemId` property must be specified. | The request is missing a required `itemId` property, which specifies the unique ID of the item being triggered. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. Request is missing workflow step definition. | The request is missing a required workflow step. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. `triggerOnItem` property must be specified. | The request is missing a required `triggerOnItem` property, which specifies the type of item that triggers a workflow step. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. `workflowStepId` is malformed. | The `workflowStepId` in the request is not a valid [GUID](http://guid.one/). |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. `workflowStepId` must be defined. | The request is missing a workflow step ID, which is required. |
| INVALID\_REQUEST\_PARAMETER | The request contained at least one invalid parameter. `workflowStepId` must not be specified during step creation, a new step id will be generated in the response. | A request to create a new workflow step includes a step ID, but it should not. |
| WORKFLOW\_UPDATE\_NOT\_ALLOWED | Update to the workflow is not allowed. Delayed Routing delay has already elapsed, unable to modify Delayed Routing delay. | The request workflow defines a `delayedRouting delay` rule that differs from the current state of the workflow's `delayedRouting delay` rule for the same workflow step, and the current `delayedRouting delay` has already elapsed. |
| WORKFLOW\_UPDATE\_NOT\_ALLOWED | Update to the workflow is not allowed. Unable to delete workflow step, a delayed routing delay is either in progress or completed. | A request to delete a workflow step could not be completed because a delayed routing countdown has started or finished. For a countdown in progress, an [EnvelopeWorkflowDefinition:updateEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopedelayedroutingdefinition/) request can be used to update the delay or send time to one minute in the future, effectively ending the delay. |
| WORKFLOW\_UPDATE\_NOT\_ALLOWED | Update to the workflow is not allowed. Unable to delete workflow step, step has already been processed. | A request to delete a workflow step could not be completed because the step is finished. |
| WORKFLOW\_UPDATE\_NOT\_ALLOWED | Update to the workflow is not allowed. Unable to delete delay, delay step is either in progress or completed. | A request to delete delayed routing from a workflow step could not be completed because the delayed routing countdown has started or finished. For a countdown in progress, an [EnvelopeWorkflowDefinition:updateEnvelopeDelayedRoutingDefinition](https://developers.docusign.com/docs/esign-rest-api/reference/envelopes/envelopeworkflowdefinition/updateenvelopedelayedroutingdefinition/) request can be used to update the delay or send time to one minute in the future, effectively ending the delay. |
| WORKFLOW\_UPDATE\_RECIPIENTROUTING\_NOT\_ALLOWED | This Account lacks sufficient permissions. | The request contains delayed routing rules, but the requesting user's account does not have delayed routing available in their account plan. |

## Next steps

For details and example code that demonstrates how to delay routing for an envelope, see:

- [How to send an envelope with delayed routing](https://developers.docusign.com/docs/esign-rest-api/how-to/send-envelope-with-delayed-routing/)

For information about delaying routing for an envelope in the [eSignature web application](https://account-d.docusign.com/), see:

- [Add Delays Between Recipients in a Routing Order﻿](https://support.docusign.com/s/document-item?&bundleId=gav1643676262430&topicId=vvh1648171137681.html)

For more features of Advanced Recipient Routing, see:

- [Scheduled sending](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/scheduled-sending/)
- [How to schedule an envelope](https://developers.docusign.com/docs/esign-rest-api/how-to/schedule-an-envelope/)
- [Pause and unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/pause-unpause-workflow/)
- [How to pause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/pause-workflow/)
- [How to unpause a signature workflow](https://developers.docusign.com/docs/esign-rest-api/how-to/unpause-workflow/)
- [Specify conditional recipients](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/recipients/conditional-recipients/)
- [How to use conditional recipients](https://developers.docusign.com/docs/esign-rest-api/how-to/use-conditional-recipients/)

For information about bulk sending, see:

- [Bulk sending envelopes](https://developers.docusign.com/docs/esign-rest-api/esign101/concepts/envelopes/bulk-send/)
- [How to bulk send envelopes](https://developers.docusign.com/docs/esign-rest-api/how-to/bulk-send-envelopes/)

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
