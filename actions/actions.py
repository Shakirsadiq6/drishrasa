# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class ActionWelcomeMessage(Action):

    def name(self) -> Text:
        return "action_welcome_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Hi Chappie here😎, your virtual assistant.👋"
        response2 = "What brought you here today?"
        welcomebuttons = ['I have questions 🙂', 'Just browsing 🙄']

        buttons = []
        for i in welcomebuttons:
            buttons.append({"title": i, "payload": i})
        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons=buttons)
        return []

class ActionQuestions(Action):

    def name(self) -> Text:
        return "action_ihavequestions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "I'll be more than happy to answer all your questions!"
        response2 = "What information are you looking for?"
        questionbuttons = ['🤝Contact sales', '🚀 Features', '⚙ Integrations', '📧 Reach us']

        buttons = []
        for i in questionbuttons:
            buttons.append({"title": i, "payload": i})
        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons=buttons)
        return []

class ActionJustBrowsing(Action):

    def name(self) -> Text:
        return "action_justbrowsing"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Got it! If you have any other questions, feel free to start the chat again. 🙌"
        response2 = "Have fun browsing our website! 👋"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        return []

class ActionContactSales(Action):

    def name(self) -> Text:
        return "action_contactsales"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Before we start, please answer the following questions."
        response2 = "Do you agree to have your personal data processed?"
        response3 = "ℹ To see our Privacy Policy, select the button below."

        salesbuttons = ['👍 I agree', '👎 I do not agree', '📃 Privacy policy']

        buttons = []
        for i in salesbuttons:
            buttons.append({"title": i, "payload": i})

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        dispatcher.utter_message(text= response3, buttons=buttons)
        return []

class ActionIAgree(Action):

    def name(self) -> Text:
        return "action_iagree"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Great! 💪"
        response2 = "I just need more information to find the right person for you. 😊"
        response3 = "what's your phone number?"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        dispatcher.utter_message(text= response3)
        return []

class ActionDontAgree(Action):

    def name(self) -> Text:
        return "action_idontagree"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dontagreebuttons = ['👈 Go to main menu', '🤔 I have changed my mind']

        buttons = []
        for i in dontagreebuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "Got it!"
        response2 = "What would you like to do next?"
        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons= buttons)
        return []

class ActionIntegrations(Action):

    def name(self) -> Text:
        return "action_integrations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        integrationbuttons = ['🤝Contact sales', '👈 Go to main menu']

        buttons = []
        for i in integrationbuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "We offers integrations with websites, mobile apps, and also with other popular apps like FB, LI, TW and more."
        response2 = "Want to know more?"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons= buttons)
        return []

class ActionIntegrations(Action):

    def name(self) -> Text:
        return "action_contactus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        email_link ='''<a href='mailto: chatbots@drishinfo.com' style="color:#0000FF;"> chatbots.drishinfo.com </a>'''
        website_link ='''<a href='https://www.drishinfo.com/' target="_blank" style="color:#0000FF;"> www.drishinfo.com </a>'''
        response1 = f"For more info reach us at {email_link} or you can visit our website {website_link}"
        dispatcher.utter_message(text= response1)
        return []

class ActionCustomerName(Action):

    def name(self) -> Text:
        return "action_customer_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Got it! If you have any other questions, feel free to start the chat again. 🙌"
        response2 = "Have fun browsing our website! 👋"

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        return []

class ActionEmail(Action):

    def name(self) -> Text:
        return "action_email"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        emailbuttons = ['🤝Contact sales', '👈 Go to main menu']

        buttons = []
        for i in emailbuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "Thank you! 👍 Our representative will get back to you within 48 hours.😊"
        response2 = "What would you like to do next?"

        # All the previous messages
        chat_list = []
        for event in tracker.events:
            if event.get("event") == "user":
                if "Customer: " in str(event.get("text")) or "Bot: " in str(event.get("text")):
                    chat_list.append(str(event.get("text")))
                    continue
                else:
                    content = "Customer: "+str(event.get("text"))
                    chat_list.append(content)

            if event.get("event") == "bot":
                if "Bot: " in str(event.get("text")) or "Customer: " in str(event.get("text")):
                    chat_list.append(str(event.get("text")))
                    continue
                else:
                    content = "Bot: "+str(event.get("text"))
                    chat_list.append(content)

        chat_list = [x for x in chat_list if x is not None]
        final_filtered_chat = list(dict.fromkeys(chat_list))

        to_email = "chatbots@drishinfo.com"
        sender_email = "chatbots@drishinfo.com"
        msg = MIMEMultipart()
        msg['From'] = to_email
        msg['To'] = sender_email
        msg['Subject'] = "Prospective Customer | Enquiry raised on https://chatbots.drishinfo.com/"

        body = "\r\n".join(final_filtered_chat)
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP("mail.drishinfo.com",587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("chatbots@drishinfo.com", "GTbb39n2zJJ46")
        text = msg.as_string()
        server.sendmail(to_email, sender_email, text)

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons= buttons)
        return []

class ActionEmailToUser(Action):

    def name(self) -> Text:
        return "action_email_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # All the previous messages
        user_input = []
        for event in tracker.events:
            if event.get("event") == "user":
                user_input.append(event.get("text"))

        our_email = "chatbots@drishinfo.com"
        user_email = user_input[-1]

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Message From Chatbots Drish Infotech Pvt. Ltd."
        msg['From'] = our_email
        msg['To'] = user_email

        html = """\
<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">

<head>
    <title></title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <meta content="width=device-width,initial-scale=1" name="viewport" />
    <!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]-->
    <style>
        * {
            box-sizing: border-box
        }

        body {
            margin: 0;
            padding: 0
        }

        a[x-apple-data-detectors] {
            color: inherit !important;
            text-decoration: inherit !important
        }

        #MessageViewBody a {
            color: inherit;
            text-decoration: none
        }

        p {
            line-height: inherit
        }

        .desktop_hide,
        .desktop_hide table {
            mso-hide: all;
            display: none;
            max-height: 0;
            overflow: hidden
        }

        @media (max-width:720px) {
            .desktop_hide table.icons-inner {
                display: inline-block !important
            }

            .icons-inner {
                text-align: center
            }

            .icons-inner td {
                margin: 0 auto
            }

            .image_block img.big,
            .row-content {
                width: 100% !important
            }

            .mobile_hide {
                display: none
            }

            .stack .column {
                width: 100%;
                display: block
            }

            .mobile_hide {
                min-height: 0;
                max-height: 0;
                max-width: 0;
                overflow: hidden;
                font-size: 0
            }

            .desktop_hide,
            .desktop_hide table {
                display: table !important;
                max-height: none !important
            }
        }
    </style>
</head>

<body style="background-color:#f9f9f9;margin:0;padding:0;-webkit-text-size-adjust:none;text-size-adjust:none">
    <table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation"
        style="mso-table-lspace:0;mso-table-rspace:0;background-color:#f9f9f9" width="100%">
        <tbody>
            <tr>
                <td>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1"
                        role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0"
                                        class="row-content stack" role="presentation"
                                        style="mso-table-lspace:0;mso-table-rspace:0;color:#000;width:600px"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="background: #4da6e7; mso-table-lspace:0;mso-table-rspace:0;font-weight:400;text-align:left;vertical-align:top;padding-top:5px;padding-bottom:5px;border-top:0;border-right:0;border-bottom:0;border-left:0"
                                                    width="100%">
                                                    <table border="0" cellpadding="0" cellspacing="0"
                                                        class="image_block" role="presentation"
                                                        style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                                                        <tr>
                                                            <td
                                                                style="padding-bottom:15px;padding-top:15px;width:100%;padding-right:0;padding-left:0; background: #4da6e7;">
                                                                <div align="center" style="line-height:10px"><img
                                                                        alt="Alternate text" src="https://drive.google.com/uc?export=download&id=1UtAZy85aGlUWPRC1C4CoXz5OjRGI7HN5"
                                                                        style="display:block;height:auto;border:0;width:189px;max-width:100%"
                                                                        title="Alternate text" width="195" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2"
                        role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0"
                                        class="row-content stack" role="presentation"
                                        style="mso-table-lspace:0;mso-table-rspace:0;color:#000;width:600px"
                                        width="350">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace:0;mso-table-rspace:0;font-weight:400;text-align:left;vertical-align:top;padding-top:0;padding-bottom:0;border-top:0;border-right:0;border-bottom:0;border-left:0"
                                                    width="100%">
                                                    <table border="0" cellpadding="0" cellspacing="0"
                                                        class="image_block" role="presentation"
                                                        style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                                                        <tr>
                                                            <td style="width:100%;padding-top:60px; padding-bottom:60px; padding-left:0">
                                                                <div align="center" style="line-height:10px"><img
                                                                        alt="Alternate text" class="big"
                                                                        src="https://drive.google.com/uc?export=download&id=1Ny-bkfuESj7a-LeA10635OKr5C4e4R-U"
                                                                        style="display:block;height:auto;border:0;max-width:350px; width:100%"
                                                                        title="Alternate text" width="350" /></div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3"
                        role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0"
                                        class="row-content stack" role="presentation"
                                        style="mso-table-lspace:0;mso-table-rspace:0;background-color:rgb(241, 241, 241);color:#000;width:600px"
                                        width="700">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1"
                                                    style="mso-table-lspace:0;mso-table-rspace:0;font-weight:400;text-align:left;vertical-align:top;padding-top:5px;padding-bottom:5px;border-top:0;border-right:0;border-bottom:0;border-left:0"
                                                    width="100%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="text_block"
                                                        role="presentation"
                                                        style="mso-table-lspace:0;mso-table-rspace:0;word-break:break-word"
                                                        width="100%">
                                                        <tr>
                                                            <td
                                                                style="padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:25px">
                                                                <div style="font-family:sans-serif">
                                                                    <div class="txtTinyMce-wrapper"
                                                                        style="font-size:12px;mso-line-height-alt:18px;color:#34495e;line-height:1.5;font-family:Montserrat,Trebuchet MS,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Tahoma,sans-serif">
                                                                        <p
                                                                            style="margin:0;font-size:16px;text-align:center;mso-line-height-alt:42px">
                                                                            <span style="font-size:28px;"><strong>Thanks
                                                                                    for reaching out.
                                                                                </strong></span>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="text_block"
                                                        role="presentation"
                                                        style="mso-table-lspace:0;mso-table-rspace:0;word-break:break-word"
                                                        width="100%">
                                                        <tr>
                                                            <td
                                                                style="padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:10px">
                                                                <div style="font-family:sans-serif">
                                                                    <div class="txtTinyMce-wrapper"
                                                                        style="font-size:12px; padding-left:18px; padding-right:18px;  mso-line-height-alt:18px;color:grey;line-height:1.7;font-family:Montserrat,Trebuchet MS,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Tahoma,sans-serif">
                                                                        <p
                                                                            style="margin:0;font-size:14px;text-align:center">
                                                                            Your details have been submitted! We'll get
                                                                            back to you shortly. Meanwhile, for any
                                                                            query feel free to reach us at <a
                                                                                style="color: #4da6e7"
                                                                                href="chatbots@drishinfo.com"
                                                                                target="_blank">chatbots@drishinfo.com</a>
                                                                        </p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>

                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>


                </td>
            </tr>
        </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-10" role="presentation"
        style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
        <tbody>
            <tr>
                <td>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack"
                        role="presentation"
                        style="mso-table-lspace:0;mso-table-rspace:0;background-color:rgb(241, 241, 241);color:#000;width:600px"
                        width="700">
                        <tbody>
                            <tr>
                                <td class="column column-1"
                                    style="mso-table-lspace:0;mso-table-rspace:0;font-weight:400;text-align:left;vertical-align:top;padding-top:5px;padding-bottom:5px;border-top:0;border-right:0;border-bottom:0;border-left:0"
                                    width="100%">
                                    <table border="0" cellpadding="0" cellspacing="0" class="divider_block"
                                        role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                                        <tr>
                                            <td
                                                style="padding-bottom:10px;padding-left:10px;padding-right:10px;padding-top:25px">
                                                <div align="center">
                                                    <table border="0" cellpadding="0" cellspacing="0"
                                                        role="presentation"
                                                        style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                                                        <tr>
                                                            <td class="divider_inner"
                                                                style="font-size:1px;line-height:1px;border-top:1px solid #bbb; ">
                                                                <span> </span>
                                                                <p class="text"
                                                                    style="color:rgb(0, 0, 0);  font-family:'Open Sans',Helvetica,Arial,sans-serif;font-size:13px;font-weight:400;font-style:italic;letter-spacing:normal;line-height:22px;text-transform:none;text-align:center;padding:10px;margin:0">
                                                                    <b>Note:</b> You are receving this
                                                                    email because recently you have
                                                                    raised a query at
                                                                    chatbots.drishinfo.com</p>

                                                            </td>
                                                        </tr>

                                                    </table>


                                                </div>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>


    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-13" role="presentation"
        style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
        <tbody>
            <tr>
                <td>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack"
                        role="presentation"
                        style="mso-table-lspace:0;mso-table-rspace:0;background-color:#34495e;color:#000;width:600px"
                        width="700">
                        <tbody>
                            <tr>
                                <td class="column column-1"
                                    style="mso-table-lspace:0;mso-table-rspace:0;font-weight:400;text-align:left;vertical-align:top;border-top:0;border-right:0;border-bottom:0;border-left:0"
                                    width="50%">

                                </td>
                                <td class="column column-2"
                                    style="mso-table-lspace:0;mso-table-rspace:0;font-weight:400;text-align:left;vertical-align:top;border-top:0;border-right:0;border-bottom:0;border-left:0"
                                    width="50%">

                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-14" role="presentation"
        style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
        <tbody>
            <tr>
                <td>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack"
                        role="presentation" style="mso-table-lspace:0;mso-table-rspace:0;color:#000;width:600px"
                        width="700">
                        <tbody>
                            <tr>
                                <td class="column column-1"
                                    style="mso-table-lspace:0;  background:rgb(241, 241, 241); mso-table-rspace:0;font-weight:400;text-align:left;vertical-align:top;padding-top:5px;padding-bottom:5px;border-top:0;border-right:0;border-bottom:0;border-left:0"
                                    width="100%">
                                    <table border="0" cellpadding="0" cellspacing="0" class="icons_block"
                                        role="presentation" style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                                        <tr>
                                            <td
                                                style="vertical-align:middle;color:#9d9d9d; inherit;font-size:15px;padding-bottom:5px;padding-top:5px;text-align:center">
                                                <table cellpadding="0" cellspacing="0" role="presentation"
                                                    style="mso-table-lspace:0;mso-table-rspace:0" width="100%">
                                                    <tr>
                                                        <td style="vertical-align:middle;text-align:center">
                                                            <!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
                                                            <!--[if !vml]><!-->
                                                            <table cellpadding="0" cellspacing="0" class="icons-inner"
                                                                role="presentation"
                                                                style="mso-table-lspace:0;mso-table-rspace:0;display:inline-block;margin-right:-4px;padding-left:0;padding-right:0">
                                                                <!--<![endif]-->
                                                                <tr>
                                                                    <td
                                                                        style="font-family:Montserrat,Trebuchet MS,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Tahoma,sans-serif;font-size:15px;color:#000000;vertical-align:middle;letter-spacing:undefined;text-align:center"> © Chatbots |<a href="https://www.drishinfo.com/"
                                                                            style="color: #000000; text-decoration: none;"
                                                                            target="_blank">Drish
                                                                            Infotech 2022</a>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </td>
            </tr>
        </tbody>

    </table><!-- End -->
</body>
</html>
        """

        part1 = MIMEText(html, 'html')

        msg.attach(part1)
        mail = smtplib.SMTP("mail.drishinfo.com",587)

        mail.ehlo()

        mail.starttls()

        mail.login(our_email, 'GTbb39n2zJJ46')
        mail.sendmail(our_email, user_email, msg.as_string())
        mail.quit()

        dispatcher.utter_message(text="")

class ActionFeatures(Action):

    def name(self) -> Text:
        return "action_features"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        featuresbuttons = ['😍 Conversational UI', '📈 Grows Revenue', '🤩 Improve customer acquisition']

        buttons = []
        for i in featuresbuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "Chatbots provides a wide range of features that let you automate your customer communication with ease."
        response2 = "Pick the one you like to know more about."

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2, buttons= buttons)
        return []

class ActionConversationalUI(Action):

    def name(self) -> Text:
        return "action_conversationalui"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cuibuttons = ['🤝Contact sales', '👈 Go to main menu', '🔙 Go back to features']

        buttons = []
        for i in cuibuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "A powerful"+'''<a><b> conversational interface</b></a>'''+" pushes the brand for deeper levels of engagement with their customers."

        dispatcher.utter_message(text= response1, buttons= buttons)
        return []

class ActionGrowthRevenue(Action):

    def name(self) -> Text:
        return "action_growthrevenue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        grbuttons = ['🤝Contact sales', '👈 Go to main menu', '🔙 Go back to features']

        buttons = []
        for i in grbuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "With smart and reliable responses, customers will feel happy and satisfied with services, which means"+'''<a><b> higher conversion rates.</b></a>'''

        dispatcher.utter_message(text= response1, buttons= buttons)
        return []

class ActionCustomerAcquisition(Action):

    def name(self) -> Text:
        return "action_customeracquisition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cabuttons = ['🤝Contact sales', '👈 Go to main menu', '🔙 Go back to features']

        buttons = []
        for i in cabuttons:
            buttons.append({"title": i, "payload": i})

        response1 = "Faster response time, 24/7 customer support & high degree of accuracy resulting in "+'''<a><b> high-quality support.</b></a>'''

        dispatcher.utter_message(text= response1, buttons= buttons)
        return []

class ActionPrivacyPolicy(Action):

    def name(self) -> Text:
        return "action_privacypolicy"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "Click the below link to check our privacy policy"
        response2 = '''<a href='https://www.drishinfo.com/privacy-policy/' style="color:#0000FF;">https://www.drishinfo.com/privacy-policy</a>'''
        response3 = "Do you agree to have your personal data processed?"
        privacy_buttons = ['👍 I agree', '👎 I do not agree']

        buttons = []
        for i in privacy_buttons:
            buttons.append({"title": i, "payload": i})

        dispatcher.utter_message(text= response1)
        dispatcher.utter_message(text= response2)
        dispatcher.utter_message(text= response3, buttons=buttons)
        return []

class ActionPhonenumber(Action):

    def name(self) -> Text:
        return "action_phonenumber"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response1 = "What's your business email address?"

        dispatcher.utter_message(text= response1)
        return []