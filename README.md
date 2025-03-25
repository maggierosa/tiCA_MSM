# Time-independent Component Analysis and Markov State Modeling Scripts 
Margarida Rosa, Shana Bergman at Weill Cornell Medicine. 

## Author Information
- **Authors**: MR, SB, AR (Latest Update: Mar 25, 2025) 
- **Contact Information**: MR (mar4026@med.cornell.edu)
If you have any questions or notice any mistakes, please contact us.

## Description
This script allows users to build time-lagged Independent Component Analysis (tICA), a dimensionality reduction technique specifically designed for time-series data, like molecular dynamics simulations. It identifies the slowest-changing components (or collective variables) in the system, which are often the most biologically relevant. By projecting high-dimensional trajectory data onto these slow modes, tICA helps isolate key conformational changes and transitions.
Markov State Models (MSMs) provide a statistical framework to model the kinetics of molecular systems. MSMs discretize the conformational space into states and estimate transition probabilities between them over a given lag time. This allows researchers to:

Please refer to the following papers: 

**For theoretical background on tiCA and MSMs:**
- Naritomi, Yusuke, and Sotaro Fuchigami. ‘Slow Dynamics in Protein Fluctuations Revealed by Time-Structure Based Independent Component Analysis: The Case of Domain Motions’. The Journal of Chemical Physics 134, no. 6 (14 February 2011): 065101. https://doi.org/10.1063/1.3554380.
- Schultze, Steffen, and Helmut Grubmüller. ‘Time-Lagged Independent Component Analysis of Random Walks and Protein Dynamics’. Journal of Chemical Theory and Computation 17, no. 9 (14 September 2021): 5766–76. https://doi.org/10.1021/acs.jctc.1c00273.
- Wang, Wei, Siqin Cao, Lizhe Zhu, and Xuhui Huang. ‘Constructing Markov State Models to Elucidate the Functional Conformational Changes of Complex Biomolecules’. WIREs Computational Molecular Science 8, no. 1 (January 2018). https://doi.org/10.1002/wcms.1343.
Pérez-Hernández, Guillermo, Fabian Paul, Toni Giorgino, Gianni De Fabritiis, and Frank Noé. ‘Identification of Slow Molecular Order Parameters for Markov Model Construction’. The Journal of Chemical Physics 139, no. 1 (7 July 2013): 015102. https://doi.org/10.1063/1.4811489.
**For Applications done in our Lab:**
- Razavi, Asghar M., George Khelashvili, and Harel Weinstein. ‘A Markov State-Based Quantitative Kinetic Model of Sodium Release from the Dopamine Transporter’. Scientific Reports 7, no. 1 (6 January 2017): 40076. https://doi.org/10.1038/srep40076.
- Morra, Giulia, Asghar M. Razavi, Anant K. Menon, and George Khelashvili. ‘Cholesterol Occupies the Lipid Translocation Pathway to Block Phospholipid Scrambling by a G Protein-Coupled Receptor’. Structure (London, England: 1993) 30, no. 8 (4 August 2022): 1208-1217.e2. https://doi.org/10.1016/j.str.2022.05.010.  

## Usage
This pipeline is intended for use following the Collective Variable Analysis by DS (on Frontier/Andes), as the input CV files are specifically formatted to match the output of that workflow. However, the pipeline can be adapted to accommodate other input formats with minimal modifications.
🔒 Private repository – accessible to members of the GK and HW labs.
📁 Repository link: https://github.com/weinsteinlab/collective_variable_parallel_rhea
