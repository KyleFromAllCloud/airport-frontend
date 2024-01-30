import streamlit as st
import subprocess
import boto3

# AWS CLI configuration
aws_access_key_id = st.secrets["aws_access_key_id"]
aws_secret_access_key = st.secrets["aws_secret_access_key"]
aws_region = "us-east-1"

# Streamlit app
st.title("Lex Intent Modifier")

# Accept freeform text input
user_input = st.text_area("Please Enter new Intent Response:")

if st.button("Run AWS CLI Command"):
    # Validate input
    if not user_input:
        st.error("Please Enter new Intent Response.")
    else:
        # try:
            # Create an S3 client using boto3 with the loaded credentials
        session = boto3.client(
            'lexv2-models',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )
        intent_params = {
                'intentId': 'W05NGSLJ6J',
                'intentName': 'wheelchair',
                "sampleUtterances": [
                    {
                        "utterance": "I need a wheelchair"
                    },
                    {
                        "utterance": "I will need a wheelchair when I arrive at the airport for my departing flight. How do I get one?"
                    },
                    {
                        "utterance": "who do I get a wheelchair"
                    },
                    {
                        "utterance": "can you help me get a wheel chair"
                    },
                    {
                        "utterance": "i need a wheelchair when I get to the airport"
                    },
                    {
                        "utterance": "how do i get a wheelchair when I get to the airport"
                    },
                    {
                        "utterance": "where can I get a wheelchair"
                    },
                    {
                        "utterance": "how do I get a wheelchair"
                    }
                ],
                'localeId': 'en_US',
                'botId': '7LIOJYDHIB',
                'botVersion': 'DRAFT',
                'initialResponseSetting': {
                    'initialResponse': {
                        'messageGroups': [
                            {
                                'message': {
                                    'plainTextMessage': {
                                        'value': user_input
                                    }
                                }
                            }
                        ],
                        'allowInterrupt': True
        },
        "nextStep": {
            "dialogAction": {
                "type": "EndConversation"
            }
                    }
                }
            }
        # List objects in the specified S3 bucket
        objects = session.update_intent(**intent_params)
        output = session.build_bot_locale(
            botId='7LIOJYDHIB',
            botVersion='DRAFT',
            localeId='en_US'
        )

        # Display the result
        st.subheader("Logs:")
        st.write(output)
            # else:
            #     st.write("No objects found in the specified bucket.")

        # except Exception as e:
        #     st.error(f"An error occurred: {str(e)}")
