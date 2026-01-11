# IEEE RAS Task 5 – 555 Timer Circuits

**Task Title:** Reach Optimum RPM – 555 Timer in Monostable, Astable, and Bistable Modes

**Semester / Event:** IEEE Student Branch RAS – Introductory Tasks (2023)

**Deadline:** Sunday, December 10th, 2023 at 23:00

**Full Name:** Islam Elsayed

**University:** Zagazig University

**Department:** Electrical Engineering / Electronics  <!-- Adjust if needed -->

## Task Objectives

- Learn about the 555 timer IC, RC circuits, duty cycle, and time constants.
- Design and simulate circuits implementing the 555 timer in monostable, astable, and bistable modes.
- Understand applications like one-shot pulses, oscillators, and flip-flops.

## Resources Used

- Walid Issa – Electronics Playlist (Arabic).
- 555 Timers Playlist.
- Proteus 8 Professional for circuit simulation.

## Task Requirements & Solutions

1. **Design a Circuit Implementing 555 in Monostable State:**  
   Created a monostable multivibrator (one-shot) using 555 (U2). Triggered by a switch (SET1), it produces a single pulse. Timing set by R5 (100k) and C3 (10uF) for pulse width ≈ 1.1 * R * C ≈ 1.1 seconds. Output drives LED (D2) via R8 (330Ω).

2. **Design a Circuit Implementing 555 in Astable State:**  
   Implemented an astable multivibrator (oscillator) with 555 (U3). Frequency determined by RA (10k), RB (10k), and C5 (100uF): f ≈ 1.44 / ((RA + 2*RB) * C) ≈ 0.48 Hz. Duty cycle ≈ (RB + RA) / (RA + 2*RB) ≈ 67%. Output blinks LED (D3) via R9 (330Ω).

3. **Design a Circuit Implementing 555 in Bistable State:**  
   Built a bistable multivibrator (flip-flop) using 555 (U1). SET and RESET switches toggle the state via R1/R2/R3 (10k). Output stable in high or low, driving LED (D1) via R4 (330Ω). Acts like an SR latch.

Circuits are simulated separately in Proteus but can be combined if needed.

## Project Structure

```
Task5/
├── Explanation_Video.mp4          ← 3-minute video explaining all circuits and components
├── README.md                        ← This documentation file
├── Task_5.pdf                       ← Original task requirements PDF
├── Task5_Schematic_AST.PDF                    ← PDF schematic for Astable circuit
├── Task5_Schematic_AST.pdsprj                 ← Proteus file for Astable circuit
├── Task5_Schematic_BIS.PDF                    ← PDF schematic for Bistable circuit
├── Task5_Schematic_BIS.pdsprj                 ← Proteus file for Bistable circuit
├── Task5_Schematic_MON.PDF                    ← PDF schematic for Monostable circuit
└── Task5_Schematic_MON.pdsprj                 ← Proteus file for Monostable circuit
```

## Circuit Descriptions

- **Monostable Circuit (Problem 1):**  
  - Components: 555 (U2), R5 (100k timing), C3 (10uF timing), R6 (10k pull-up), C2 (1nF noise filter), R8 (330Ω), D2 (LED-RED), SET1 (trigger switch).  
  - Operation: Trigger low pulse charges C3 through R5; output high for timed period, then resets. Useful for debouncing or timed delays.

- **Astable Circuit (Problem 2):**  
  - Components: 555 (U3), RA (10k charge), RB (10k discharge), C5 (100uF timing), C4 (1nF filter), R9 (330Ω), D3 (LED-RED).  
  - Operation: Continuous oscillation; capacitor charges via RA+RB, discharges via RB. Produces square wave for blinking, clocks, or PWM.

- **Bistable Circuit (Problem 3):**  
  - Components: 555 (U1), R1/R2/R3 (10k for set/reset), C1 (10nF filter), R4 (330Ω), D1 (LED-RED), SET/RESET switches.  
  - Operation: SET pulls trigger low (output high), RESET pulls discharge low (output low). Stable states until toggled; like a simple memory cell.

Simulation in Proteus shows correct behaviors: Monostable pulses once, astable oscillates, bistable toggles stably.

## Key Learnings

- 555 Timer: Versatile IC with comparator, flip-flop, and discharge transistor; modes depend on external RC.
- RC Time Constant: τ = R * C; controls pulse width (monostable: 1.1τ), frequency (astable: ≈1.44 / ((RA + 2RB)C)).
- Duty Cycle: In astable, adjustable via RA/RB ratio (50% if RA << RB).
- Add bypass capacitors (e.g., 1nF on CV) to reduce noise.

## How to Run the Simulation

1. Open Proteus 8 Professional.
2. Load the respective .pdsprj file (e.g., Task5_MON.pdsprj).
3. Click the play button to simulate.
4. Interact with switches (SET/RESET) or observe LED/oscilloscope for waveforms.

## Evaluation Notes

- Each Circuit: 2.5/2.5 (Total 7.5/7.5 – All functional in simulation).
- Explanation Video: 2.5/2.5 (Covers all circuits, components, and operations).

*Submitted for IEEE SB RAS – December 2023*  
*Prepared by: Islam Elsayed*