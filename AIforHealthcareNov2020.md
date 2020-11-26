# AI for Healthcare workshop (Nov 26-27, 2020)

      * [Class Activation Mapping](http://cnnlocalization.csail.mit.edu/Zhou_Learning_Deep_Features_CVPR_2016_paper.pdf): "the predicted class score is mapped back to the previous convolutional layer to generate the class activation maps" 
      * Idea: sequence -> image
        * Engine inspection using running noise: speech -> spectogram -> analyzed using CNN
        * DNA sequence -> color image: upto 16M necleotides
          * perhaps, 1D-to-2D mapping may affect short- and long-term dependency. (Some may be enhanced. Some may be hindered.) 
      * [Ciracore](https://www.facebook.com/groups/cira.core.comm/) (AI platform, run on Ubuntu)
         * [PC (Ubuntu 16.04)](https://git.cira-lab.com/cira/cira-core)
         * [Jetson (Jetpack 4.4)](https://git.cira-lab.com/cira/cira-core-nvidia-jetson)
         
      * IoT: ESP Wroom 32     
        * Raspberry Pi ~ small computer
        * Jetson Nano ~ CUDA capable
        * ESP 32 ~ cheap, requires low energy w/ WIFI and bluetooth
        * Near Field Communication (NFC) ~ close range communication (one-to-one)
        * WIFI: cons: interference among devices (currently not suitable for IoT)
        * 5G: massive MTC, critical MTC and Enhanced mobile broadband.
          * critical MTC: auto communication and remote surgery (telemedicine)
        * Data center:
          * IaaS: AWS (user can choose OS)
          * PaaS: Google App Engine, Microsoft Azure (user has to stick w/ provided OS)
          * SaaS: Dropbox (user has to stick w/ provided software)
