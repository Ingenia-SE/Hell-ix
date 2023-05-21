# MATLAB System Composer Model
The present model is aimed to provide reference for the developers taking part in the project as well as to give other people a general overview of the work. 

## Model Use and Management
All the model information is documented in the Model Final Document that can be found in <strong><code>Documentation</code></strong> folder. In this document it is also included all the information concerning model use and management. To be able to use and modify the model, it is required to have the software MATLAB installed. Additionally, the following add-ons should be installed:
- Simulink
- System Composer
- Requirements Toolbox

## Contents

- **Requirements:** requirements are assigned to the different subsystems and components of the model in order to ensure design traceability. There are three requirements files:

  - Software requirements: they are included in <strong><code>software requirements.slrqx</code></strong> file.
  - Stakeholder requirements: they are included in <strong><code>stakeholder requirements.slrqx</code></strong> file.
  - System requirements: they are included in <strong><code>system requirements.slrqx</code></strong> file.
  - Requirements traceability: the information related with the requirements assignation is included in the file <strong><code>Hell_ix_System_Architecture~mdl.slmx</code></strong>.

- **System Physical Architecture:** The physical architecture describes the hardware components together with their interconnections that enable to understand the physical model of the system. It is included in file <strong><code>Hell_ix_System_Architecture.slx</code></strong>. <strong><code>Competition.xml</code></strong> file includes information about the different stereotypes that have been created in the model, together with their assigned properties.

- **Functional Architecture:** The functional architecture describes the functional dependencies of the system as actions (each block involves certain hardware and software that enable the action to be performed). It is complementary to the main system architecture and defines how the system will behave. It is included in file <strong><code>Hell_ix_Functional_Architecture.slx</code></strong>. File <strong><code>Functional_Physical_Allocation.mldatx</code></strong> establishes traceable and directed relationships between the architectural elements of the physical and functional models.

