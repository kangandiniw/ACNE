from keras.models import load_model
from keras.preprocessing import image
from keras.layers import Input, TFSMLayer
from keras.models import Model
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from warnings import filterwarnings

# Ignore warnings
filterwarnings('ignore')

# Set global print options
np.set_printoptions(suppress=True)

# Function for face prediction
def predict_face(img_path, face_model):
    try:
        img = Image.open(img_path).convert("RGB")
        img = img.resize((128, 128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0
        
        prediction = face_model.predict(img_array, verbose=0)

        plt.imshow(img)
        plt.axis('off')
        plt.show()

        if prediction[0][0] > 0.5:
            print("Prediction: This is not a face.")
            print("Please input a face.")
            return False
        else:
            print("Prediction: This is a face.")
            print("\n")
            return True
    except Exception as e:
        print("Error during face prediction:", e)
        return False


# Function for acne presence prediction
def predict_acne_presence(img_path, acne_presence_model, labels):
    try:
        # Preprocess image
        img = Image.open(img_path).convert("RGB")
        img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
        img_array = np.asarray(img)
        normalized_img = (img_array.astype(np.float32) / 127.5) - 1
        data = np.expand_dims(normalized_img, axis=0)
        
        # Predict
        prediction = acne_presence_model.predict(data, verbose=0)

        # Debugging output
        # print("Raw Prediction:", prediction)
        if isinstance(prediction, dict):
            # print("Prediction Keys:", prediction.keys())
            # Adjust based on the actual output key
            prediction = prediction[next(iter(prediction.keys()))]

        # Interpret results
        index = np.argmax(prediction)
        acne_or_non = labels[index]
        confidence = prediction[0][index]

        print(f"Acne / Non Acne: {acne_or_non}")
        # print(f"Confidence Score: {confidence}")

        if acne_or_non == "Non Acne":
            print("Great news, your facial skin looks excellent!")
            return False
        else:
            print("Please Go To Next Step")
            print("\n")
            return True
    except Exception as e:
        print("Error during acne presence prediction:", e)
        return False

# Function for acne type prediction
def predict_acne_type(img_path, acne_type_model, labels):
    try:
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        img = Image.open(img_path).convert("RGB")
        img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
        img_array = np.asarray(img)
        normalized_img = (img_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized_img
        
        prediction = acne_type_model.predict(data, verbose=0)

        # Debugging output
        # print("Raw Prediction:", prediction)
        if isinstance(prediction, dict):
            prediction = prediction['sequential_7']  # Adjust key if needed

        # Interpret results
        index = np.argmax(prediction[0])  # Assuming the first dimension contains the prediction
        acne_type = labels[index]
        confidence = prediction[0][index]

        print(f"Acne Type: {acne_type}")
        print("\n")
        # print(f"Confidence Score: {confidence}")
        return acne_type
    except Exception as e:
        print("Error during acne type prediction:", e)
        return none

# Define the acne treatment function
def acne_treatment(acne_type):
    if acne_type == "White Comedo":
        print("Whiteheads, or closed comedones, are small or flesh-colored spots or bumps.")
        print("\nHow to Treat Whiteheads:")
            
        print("Topical Salicylic Acid:")
        print("  - Neutrogena Oil-Free Acne Wash or Cleansing Pads (e.g., Almay Clear Complexion)")
        print("  - Salicylic acid helps clear clogs and reduce excess oil.")
            
        print("\nRetinoid Use:")
        print("  - Differin Gel (Adapalene) or The Ordinary Retinol 0.2% in Squalane")
        print("  - Retinoids encourage skin cell turnover, reducing whiteheads.")
            
        print("\nClay Masks:")
        print("  - Aztec Secret Indian Healing Clay: Clay masks absorb excess oil and deep-clean pores.")
            
        print("\nGentle Exfoliation:")
        print("  - Paula's Choice 2% BHA Liquid Exfoliant for dead skin cell removal.")
            
        print("\nDIY Oatmeal Mask:")
        print("  - Mix ground oatmeal with water or honey to reduce inflammation around whiteheads.")
        print("\n")

    elif acne_type == "Nodule":
        print("Nodules are hard, inflamed lumps located deep within the skin. They are flesh-colored or red bumps that are deeper than the skin’s surface and may or may not have pus.")
        print("\nModern Medicine:")
        print("Oral Medications:")
        print("- Doxycycline:")
        print("  - Vibramycin (doxycycline hyclate): ~$10-20/month (prescription).")
        print("  - Monodox (doxycycline monohydrate): ~$15-25/month (prescription).")
        print("- Isotretinoin:")
        print("  - Accutane: ~$200-300/month (prescription).")
        print("  - Amnesteem: ~$200-300/month (prescription).")
            
        print("\nTraditional Medicine:")
        print("- Green Tea:")
        print("  - Twinings Green Tea Bags: ~$5-10 for a box of 20 bags.")
        print("  - Bigelow Green Tea: ~$5-10 for a box of 20 bags.")
        print("- Neem Oil:")
        print("  - Organic Neem Oil by NOW Solutions: ~$10-15 for a 4 oz bottle.")
        print("  - Neem Aura Naturals Neem Oil: ~$10-15 for a 2 oz bottle.")
            
        print("\nAdditional Lifestyle Suggestions:")
        print("- Skincare Routine: Use a gentle, non-comedogenic cleanser and moisturizer.")
        print("- Dietary Considerations: Focus on anti-inflammatory foods and reduce sugar and dairy intake.")
        print("- Hydration: Drink plenty of water.")
        print("- Regular Exercise: Engage in at least 30 minutes of moderate exercise most days.")
        print("- Stress Management: Practice relaxation techniques.")
        print("- Sun Protection: Use an oil-free, broad-spectrum sunscreen.")
        print("- Avoid Touching the Face.")
        print("- Regular Dermatologist Visits.")
        print("\n")

    elif acne_type == "Pustule":
        print("Pustules are larger, tender bumps with a defined circular center filled with whitish or yellowish pus. They typically look like much larger and more inflamed whiteheads.")
        print("\nModern Medicine:")
        print("Topical Treatments:")
        print("- Salicylic Acid:")
        print("  - Neutrogena Oil-Free Acne Wash: ~$7-12")
        print("  - CeraVe Renewing SA Cleanser: ~$12-15")
        print("- Retinoids:")
        print("  - Differin Gel (Adapalene): ~$10-15")
        print("  - Retinol 0.5% in Squalane by The Ordinary: ~$10")
    
        print("\nTraditional Medicine:")
        print("- Honey:")
        print("  - Manuka Honey (like Comvita Manuka Honey): ~$10-20 for a small jar.")
        print("  - Raw Honey from local sources: ~$5-10 for a bottle.")
        print("- Apple Cider Vinegar:")
        print("  - Bragg Organic Raw Apple Cider Vinegar: ~$5-10 for a 16 oz bottle.")
        print("  - Heinz Apple Cider Vinegar: ~$3-5 for a bottle.")
            
        print("\nAdditional Lifestyle Suggestions:")
        print("- Skincare Routine: Use a gentle cleanser twice daily and follow with a non-comedogenic moisturizer.")
        print("- Exfoliation: Use a chemical exfoliant like Paula's Choice 2% BHA Liquid Exfoliant: ~$30.")
        print("- Clay Masks: Aztec Secret Indian Healing Clay: ~$10 for a jar.")
        print("- Diet: Incorporate more anti-inflammatory foods and reduce processed sugars and dairy products.")
        print("- Hydration: Aim to drink at least 8 glasses of water a day.")
        print("- Stress Management: Engage in regular physical activity or mindfulness practices.")
        print("- Sun Protection: Apply EltaMD UV Clear Broad-Spectrum SPF 46: ~$40.")
        print("- Avoid Touching the Face.")
        print("\n")

    elif acne_type == "Papule":
        print("Papules are bumps under the skin’s surface that are less than 1 cm in diameter. They appear solid, tender, and raised with inflamed surrounding skin.")
        print("\nModern Medicine:")
        print("Topical Treatments:")
        print("- Benzoyl Peroxide:")
        print("  - Clearasil Ultra Rapid Action Treatment Cream: ~$10-15")
        print("  - Neutrogena On-the-Spot Acne Treatment (benzoyl peroxide 2.5%): ~$6-10")
        print("- Clindamycin:")
        print("  - Clindagel (Clindamycin Phosphate topical gel): ~$15-25 (prescription)")
        print("  - Duac Gel (Benzoyl Peroxide/Clindamycin): ~$30-50 (prescription)")
            
        print("\nTraditional Medicine:")
        print("- Tea Tree Oil:")
        print("  - The Body Shop Tea Tree Oil: ~$10-15 for a 0.5 oz bottle.")
        print("  - NOW Solutions Tea Tree Oil: ~$7-12 for a 1 oz bottle.")
        print("- Aloe Vera Gel:")
        print("  - Nature Republic Aloe Vera 92% Soothing Gel: ~$10 for a 300 ml tube.")
        print("  - Lily of the Desert Aloe Vera Gel: ~$6-8 for a 12 oz bottle.")
            
        print("\nAdditional Lifestyle Suggestions:")
        print("- Follow a consistent skincare routine:")
        print("  - Cleanse your face twice daily with a gentle, non-comedogenic cleanser like Cetaphil Gentle Skin Cleanser: ~$10.")
        print("  - Apply a non-comedogenic moisturizer, such as Neutrogena Hydro Boost Water Gel: ~$15.")
        print("  - Use a clay mask weekly to absorb excess oil and impurities, such as Aztec Secret Indian Healing Clay: ~$10.")
        print("- Diet: Focus on a balanced diet rich in fruits and vegetables. Consider reducing dairy and processed foods.")
        print("- Stay hydrated: Drink plenty of water.")
        print("- Stress management: Practice yoga, meditation, or regular exercise.")
        print("- Sun protection: Use a broad-spectrum sunscreen like Neutrogena Clear Face Sunscreen SPF 30: ~$10-15.")
        print("- Avoid touching your face or picking at papules.")
        print("\n")
        
    else : 
        print("Blackheads, or open comedones, are small, dark-colored spots that may appear as slightly raised bumps.")
        print("\nHow to Treat Blackheads:")
            
        print("Salicylic Acid Exfoliation:")
        print("  - Salicylic acid helps clean out blackheads by clearing pore blockages.")
            
        print("\nCharcoal or Clay Masks:")
        print("  - Aztec Secret Indian Healing Clay or charcoal masks work deeply to pull out oil and debris.")
            
        print("\nRegular Chemical Exfoliation:")
        print("  - Paula's Choice 2% BHA Liquid Exfoliant to reduce clogged pores and oxidation.")
            
        print("\nBaking Soda Scrub:")
        print("  - Combine baking soda with water to make a gentle scrub for opening blackheads (use sparingly).")
            
        print("\nNon-Comedogenic Oil Massage:")
        print("  - Light oils, like jojoba oil, can be used for gentle facial massage to lift blackheads naturally.")
        print("\n")

# Function for acne severity prediction
def predict_acne_severity(img_path, acne_severity_model, labels):
    try:
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        img = Image.open(img_path).convert("RGB")
        img = ImageOps.fit(img, (224, 224), Image.Resampling.LANCZOS)
        img_array = np.asarray(img)
        normalized_img = (img_array.astype(np.float32) / 127.5) - 1
        data[0] = normalized_img
        
        prediction = acne_severity_model.predict(data, verbose=0)

        # Debugging output
        # print("Raw Prediction:", prediction)
        if isinstance(prediction, dict):
            prediction = prediction['sequential_11']  # Adjust key if needed

        # Interpret results
        index = np.argmax(prediction[0])  # Assuming the first dimension contains the prediction
        severity_name = labels[index]
        confidence = prediction[0][index]

        print(f"Severity: {severity_name}")
        print("\n")
        # print(f"Confidence Score: {confidence}")
    except Exception as e:
        print("Error during acne type prediction:", e)

# Main flow
if __name__ == "__main__":
    # Load face detection model
    face_model_path = 'C:/Users/ANDINI/dataset/saved_model/my_face_classifier_model (2).h5'
    face_model = load_model(face_model_path)

    # Predict face
    face_image_path = 'C:/Users/ANDINI/dataset/saved_model/test1.jpg'
    if predict_face(face_image_path, face_model):
        # Load acne presence model
        acne_presence_model_path = "C:/Users/ANDINI/dataset/acne_nonacne/model.savedmodel"
        labels_acne_presence = open('C:/Users/ANDINI/dataset/acne_nonacne/labels.txt', "r").readlines()
        labels_acne_presence = ["Non Acne", "Acne"]
        input_shape = (224, 224, 3)
        inputs = Input(shape=input_shape)
        tfsm_layer_presence = TFSMLayer(acne_presence_model_path, call_endpoint='serving_default')
        outputs_presence = tfsm_layer_presence(inputs)
        acne_presence_model = Model(inputs=inputs, outputs=outputs_presence)
        
        if predict_acne_presence(face_image_path, acne_presence_model, labels_acne_presence):
            # Load acne type model
            acne_type_model_path = "C:/Users/ANDINI/dataset/Dataset/model.savedmodel"
            labels_acne_type = ["White Comedo", "Nodule", "Pustule", "Papule", "Black Comedo"]
            tfsm_layer_type = TFSMLayer(acne_type_model_path, call_endpoint='serving_default')
            outputs_type = tfsm_layer_type(inputs)
            acne_type_model = Model(inputs=inputs, outputs=outputs_type)

            # Predict acne type
            acne_type = predict_acne_type(face_image_path, acne_type_model, labels_acne_type)
            if acne_type:
                print(f"\nTreating {acne_type}:")
                acne_treatment(acne_type)
            else:
                print("Failed to determine acne type.")
                
            # Load acne severity model
            acne_severity_model_path = "/Users/ANDINI/dataset/saved_model/model.savedmodel"
            labels_acne_severity = ["Mild", "Moderate", "Severe", "Very Severe"]
            tfsm_layer_type = TFSMLayer(acne_severity_model_path, call_endpoint='serving_default')
            outputs_type = tfsm_layer_type(inputs)
            acne_severity_model = Model(inputs=inputs, outputs=outputs_type)

            # Predict acne severity
            acne_severity = predict_acne_severity(face_image_path, acne_severity_model, labels_acne_severity)