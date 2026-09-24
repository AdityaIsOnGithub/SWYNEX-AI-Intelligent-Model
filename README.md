# SWYNEX Task 3: Intelligent Feature & Evaluation

## Overview
This repository builds upon the Automated Plant Disease Detection prototype to fulfill Task 3 of the SWYNEX AI Internship. It introduces an interactive interface, intelligent recommendations, error handling, and model evaluation for failure cases.

## New Features Implemented
* **Simple Interface:** A Command Line Interface (CLI) menu allows users to test different model states and edge cases dynamically.
* **Intelligent Feature:** A rule-based recommendation engine that triggers upon a successful, high-confidence classification to provide immediate, actionable treatment advice (e.g., specific fungicides for 'Late Blight').
* **Failure Cases (Model Evaluation):** Simulates a scenario where the image quality is poor, resulting in low model confidence (< 70%). The system flags this failure and prompts the user to retake the photo rather than providing an inaccurate diagnosis.
* **Error Handling:** Utilizes `try/except` blocks to handle invalid file uploads (e.g., uploading a `.txt` instead of an image), preventing system crashes and returning a user-friendly error message.

## How to Run the Demo
This script uses standard Python libraries. No external dependencies are required. 
1. Run `python intelligent_disease_model.py` in your terminal.
2. Follow the on-screen CLI prompts to test the Success, Failure, and Error Handling cases.
