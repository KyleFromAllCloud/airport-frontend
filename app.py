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
{
    "intentId": "W05NGSLJ6J",
    "intentName": "wheelchair",
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
    "fulfillmentCodeHook": {
        "enabled": false,
        "postFulfillmentStatusSpecification": {
            "successResponse": {
                "messageGroups": [
                    {
                        "message": {
                            "plainTextMessage": {
                                "value": "Your wheelchair has successfully been reserved"
                            }
                        }
                    }
                ],
                "allowInterrupt": true
            },
            "failureResponse": {
                "messageGroups": [
                    {
                        "message": {
                            "plainTextMessage": {
                                "value": "I'm sorry, I must have misunderstood what you said can you please repeat."
                            }
                        }
                    }
                ],
                "allowInterrupt": true
            },
            "successNextStep": {
                "dialogAction": {
                    "type": "CloseIntent"
                },
                "intent": {}
            },
            "failureNextStep": {
                "dialogAction": {
                    "type": "CloseIntent"
                },
                "intent": {}
            },
            "timeoutNextStep": {
                "dialogAction": {
                    "type": "CloseIntent"
                },
                "intent": {}
            }
        },
        "active": true
    },
    "slotPriorities": [
        {
            "priority": 1,
            "slotId": "UZGQDOUOHY"
        }
    ],
    "intentConfirmationSetting": {
        "promptSpecification": {
            "messageGroups": [
                {
                    "message": {
                        "plainTextMessage": {
                            "value": "{Airline} offers wheelchair services, would you like me to contact them to reserve a wheelchair?"
                        }
                    }
                }
            ],
            "maxRetries": 4,
            "allowInterrupt": true,
            "messageSelectionStrategy": "Random",
            "promptAttemptsSpecification": {
                "Initial": {
                    "allowInterrupt": true,
                    "allowedInputTypes": {
                        "allowAudioInput": true,
                        "allowDTMFInput": true
                    },
                    "audioAndDTMFInputSpecification": {
                        "startTimeoutMs": 4000,
                        "audioSpecification": {
                            "maxLengthMs": 15000,
                            "endTimeoutMs": 640
                        },
                        "dtmfSpecification": {
                            "maxLength": 513,
                            "endTimeoutMs": 5000,
                            "deletionCharacter": "*",
                            "endCharacter": "#"
                        }
                    },
                    "textInputSpecification": {
                        "startTimeoutMs": 30000
                    }
                },
                "Retry1": {
                    "allowInterrupt": true,
                    "allowedInputTypes": {
                        "allowAudioInput": true,
                        "allowDTMFInput": true
                    },
                    "audioAndDTMFInputSpecification": {
                        "startTimeoutMs": 4000,
                        "audioSpecification": {
                            "maxLengthMs": 15000,
                            "endTimeoutMs": 640
                        },
                        "dtmfSpecification": {
                            "maxLength": 513,
                            "endTimeoutMs": 5000,
                            "deletionCharacter": "*",
                            "endCharacter": "#"
                        }
                    },
                    "textInputSpecification": {
                        "startTimeoutMs": 30000
                    }
                },
                "Retry2": {
                    "allowInterrupt": true,
                    "allowedInputTypes": {
                        "allowAudioInput": true,
                        "allowDTMFInput": true
                    },
                    "audioAndDTMFInputSpecification": {
                        "startTimeoutMs": 4000,
                        "audioSpecification": {
                            "maxLengthMs": 15000,
                            "endTimeoutMs": 640
                        },
                        "dtmfSpecification": {
                            "maxLength": 513,
                            "endTimeoutMs": 5000,
                            "deletionCharacter": "*",
                            "endCharacter": "#"
                        }
                    },
                    "textInputSpecification": {
                        "startTimeoutMs": 30000
                    }
                },
                "Retry3": {
                    "allowInterrupt": true,
                    "allowedInputTypes": {
                        "allowAudioInput": true,
                        "allowDTMFInput": true
                    },
                    "audioAndDTMFInputSpecification": {
                        "startTimeoutMs": 4000,
                        "audioSpecification": {
                            "maxLengthMs": 15000,
                            "endTimeoutMs": 640
                        },
                        "dtmfSpecification": {
                            "maxLength": 513,
                            "endTimeoutMs": 5000,
                            "deletionCharacter": "*",
                            "endCharacter": "#"
                        }
                    },
                    "textInputSpecification": {
                        "startTimeoutMs": 30000
                    }
                },
                "Retry4": {
                    "allowInterrupt": true,
                    "allowedInputTypes": {
                        "allowAudioInput": true,
                        "allowDTMFInput": true
                    },
                    "audioAndDTMFInputSpecification": {
                        "startTimeoutMs": 4000,
                        "audioSpecification": {
                            "maxLengthMs": 15000,
                            "endTimeoutMs": 640
                        },
                        "dtmfSpecification": {
                            "maxLength": 513,
                            "endTimeoutMs": 5000,
                            "deletionCharacter": "*",
                            "endCharacter": "#"
                        }
                    },
                    "textInputSpecification": {
                        "startTimeoutMs": 30000
                    }
                }
            }
        },
        "declinationResponse": {
            "messageGroups": [
                {
                    "message": {
                        "plainTextMessage": {
                            "value": "Okay, thank you and have a great day."
                        }
                    }
                }
            ],
            "allowInterrupt": true
        },
        "active": true,
        "confirmationNextStep": {
            "dialogAction": {
                "type": "FulfillIntent"
            },
            "intent": {}
        },
        "declinationNextStep": {
            "dialogAction": {
                "type": "EndConversation"
            },
            "intent": {}
        },
        "failureNextStep": {
            "dialogAction": {
                "type": "StartIntent"
            },
            "intent": {
                "name": "FallbackIntent"
            }
        },
        "elicitationCodeHook": {
            "enableCodeHookInvocation": true
        }
    },
    "intentClosingSetting": {
        "closingResponse": {
            "messageGroups": [
                {
                    "message": {
                        "plainTextMessage": {
                            "value": "Is there anything else I can do for you?"
                        }
                    }
                }
            ],
            "allowInterrupt": true
        },
        "active": true,
        "nextStep": {
            "dialogAction": {
                "type": "EndConversation"
            },
            "intent": {}
        }
    },
    "botId": "7LIOJYDHIB",
    "botVersion": "DRAFT",
    "localeId": "en_US",
    "creationDateTime": "2023-12-21T17:33:16.829000-05:00",
    "lastUpdatedDateTime": "2024-01-29T16:24:12.249000-05:00",
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
        },
        "nextStep": {
            "dialogAction": {
                "type": "ElicitSlot",
                "slotToElicit": "Airline"
            },
            "intent": {}
        },
        "codeHook": {
            "enableCodeHookInvocation": false,
            "active": false,
            "postCodeHookSpecification": {
                "successNextStep": {
                    "dialogAction": {
                        "type": "ConfirmIntent"
                    },
                    "intent": {}
                },
                "failureNextStep": {
                    "dialogAction": {
                        "type": "EndConversation"
                    },
                    "intent": {}
                },
                "timeoutNextStep": {
                    "dialogAction": {
                        "type": "EndConversation"
                    },
                    "intent": {}
                }
            }
        }
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
