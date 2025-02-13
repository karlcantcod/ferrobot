



**************************************

This folder controls the physical ferrobot 
logic, this includes the following:

- pico voice wakeword
- pico voice STT
- open ai api
- google cloud TTS

**************************************

As of 12th Feb 2025, my goal for this 
folder is to get an integration running
for a self hosted web app which allows
users to interact with the assistant
via a different medium.

**************************************

Control Flow:
1. Main Loop Initialization
   - Initialize Leopard SpeechToText instance
   - Start conversation clear countdown thread

2. Wake Word Detection using porcupine
   - Listen for keywords ("computer", "hey google", "alexa")
   - Activate LEDs when wake word detected
   - Play random response prompt

3. Voice Input Processing
   - Start audio recorder
   - Listen for voice input
   - Detect silence to end recording
   - Convert speech to text using Leopard

4. Response Generation
   - Start LED fade effect
   - Send transcript to ChatGPT
   - Get AI response
   - Concurrent tasks:
     * Convert response to speech (Google TTS)
     * Print response with typewriter effect
   - Stop LED fade effect

5. Error Handling
   - Handle keyboard interrupts
   - Handle API errors
   - Clean up resources on exit

6. Integration Points
   - Flask API bridge (/api/status, /api/health)
   - React frontend communication
   - GPIO control for hardware feedback

**************************************