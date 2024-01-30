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
user_input = st.text_area("Enter Intent Name:")

if st.button("Run AWS CLI Command"):
    # Validate input
    if not user_input:
        st.error("Please enter an Intent Name.")
    else:
        # try:
            # Create an S3 client using boto3 with the loaded credentials
        session = boto3.client(
            'lexv2-models',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=aws_region
        )

        # List objects in the specified S3 bucket
        objects = session.update_intent(
    "intentId": "W05NGSLJ6J",
    "intentName": "wheelchair",
    "localeId": "en_US",
    "botId": "7LIOJYDHIB",
    "botVersion": "DRAFT",
    "initialResponseSetting": {
        "initialResponse": {
            "messageGroups": [
                {
                    "message": {
                        "plainTextMessage": {
                            "value": "Wheelchair service is provided through the airlines, passengers may reserve wheelchair service in advance by calling their airline or requesting it online via their airline’s website, it is also available on demand, with services confirmed to comply with ADA and ACAA requirements."
                        }
                    }
                }
            ],
            "allowInterrupt": true
        }
        }
)

        # Display the result
        st.subheader("Objects in S3 Bucket:")
        st.write(objects)
            # else:
            #     st.write("No objects found in the specified bucket.")

        # except Exception as e:
        #     st.error(f"An error occurred: {str(e)}")
