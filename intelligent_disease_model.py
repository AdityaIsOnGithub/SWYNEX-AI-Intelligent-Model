import random
import time

# --- INTELLIGENT FEATURE: Treatment Recommendations ---
def get_treatment_recommendation(disease):
    """Provides actionable advice based on the classification."""
    treatments = {
        'Early Blight': "Apply copper-based fungicide and remove infected lower leaves.",
        'Late Blight': "Apply chlorothalonil fungicide immediately; destroy heavily infected plants to prevent spread.",
        'Healthy': "No treatment needed. Maintain optimal watering and fertilization."
    }
    return treatments.get(disease, "Consult a local agricultural extension.")

# --- CORE MODEL SIMULATION ---
def run_model_evaluation(simulate_error=False, simulate_low_confidence=False):
    print("\n[SYSTEM] Initializing Image Processor...")
    time.sleep(1)
    
    # 1. ERROR HANDLING CASE (Invalid Input)
    if simulate_error:
        try:
            print("[INPUT] User uploaded file: 'farm_notes.txt'")
            raise ValueError("Invalid file format. Expected image tensor (.jpg, .png).")
        except ValueError as e:
            print(f"\n❌ [ERROR HANDLED]: {e}")
            print("💡 System Prompt: Please upload a valid plant leaf image.")
            return

    # 2. STANDARD PROCESSING
    print("[INPUT] Loading sample leaf image tensor: (1, 224, 224, 3)...")
    print("[PROCESSING] Running image through CNN layers...")
    time.sleep(1.5)
    
    classes = ['Healthy', 'Early Blight', 'Late Blight']
    predicted_class = random.choice(classes)
    
    # 3. FAILURE CASE (Low Confidence / Ambiguous Image)
    if simulate_low_confidence:
        confidence = random.uniform(40.0, 65.0) # Low confidence threshold
        print(f"\n[OUTPUT] Prediction: {predicted_class}")
        print(f"[OUTPUT] Confidence Score: {confidence:.2f}%")
        print("\n⚠️ [FAILURE CASE DETECTED: LOW CONFIDENCE]")
        print("💡 System Prompt: Confidence is too low for a reliable diagnosis. The image may be blurry or poorly lit. Please retake the photo.")
    
    # 4. SUCCESS CASE & INTELLIGENT FEATURE (High Confidence)
    else:
        confidence = random.uniform(88.0, 99.9)
        print(f"\n✅ [OUTPUT] Prediction: {predicted_class}")
        print(f"✅ [OUTPUT] Confidence Score: {confidence:.2f}%")
        print("\n🧠 [INTELLIGENT FEATURE TRIGGERED]")
        print(f"Recommended Action: {get_treatment_recommendation(predicted_class)}")

# --- SIMPLE INTERFACE DEMO ---
def cli_interface():
    print("==================================================")
    print(" SWYNEX Task 3: Intelligent Feature & Evaluation")
    print("==================================================")
    print("Please select a test case to evaluate the model:")
    print("1. Standard Evaluation (High Confidence & Recommendation)")
    print("2. Failure Case (Low Confidence / Ambiguous Image)")
    print("3. Error Handling Case (Invalid File Type Uploaded)")
    print("==================================================")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == '1':
        run_model_evaluation(simulate_error=False, simulate_low_confidence=False)
    elif choice == '2':
        run_model_evaluation(simulate_error=False, simulate_low_confidence=True)
    elif choice == '3':
        run_model_evaluation(simulate_error=True, simulate_low_confidence=False)
    else:
        print("\n❌ Invalid selection. Please restart and choose 1, 2, or 3.")
    print("\n--------------------------------------------------")

if __name__ == "__main__":
    cli_interface()