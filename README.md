# Computational Modeling of Bacterial Growth Using PDEs

This repository presents a mathematical model based on Partial Differential Equations (PDEs) to simulate bacterial growth, antibiotic effects, and resistance development. The model provides a continuous framework for understanding bacterial dynamics and can be used to explore infection control strategies.

## Objectives
The proposed modeling allows:

- Analyzing bacterial population dynamics over time and space.
- Simulating the effects of antibiotic administration on bacterial mortality.
- Investigating the emergence of antibiotic resistance.
- Studying the impact of environmental constraints on bacterial growth.

## Theoretical Foundation
The model is based on reaction-diffusion equations, which describe how bacterial density and antibiotic concentration change over time and space. Key references include:

- Murray, J. D. (2003). Mathematical Biology.
- Edelstein-Keshet, L. (2005). Mathematical Models in Biology.
- Turing, A. M. (1952). The Chemical Basis of Morphogenesis.

## Model Structure
The model consists of three main components:

1. **Bacterial Density**: Described by a diffusion term and a logistic growth term.
2. **Antibiotic Concentration**: Diffuses through the environment and kills bacteria.
3. **Resistance Development**: A fraction of bacteria exposed to antibiotics develop resistance.

## Running the Simulation
### 1. Cloning the Repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/Computing-Epidemiology.git
   ```

### 2. Environment Configuration
Ensure you have Python installed. Install the necessary dependencies with:

pip install numpy matplotlib scipy

### 3. Running the Model
Execute the main script:

python main.py

This will generate a dynamic visualization of bacterial growth and antibiotic effects.

## Scientific Considerations
This model provides a continuous and scalable framework for studying bacterial dynamics. It can be extended to include additional factors such as immune responses, nutrient availability, and multi-drug resistance.