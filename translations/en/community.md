# Community and contributions

AlohaMini was created by **Li Yiteng** and **Wu Zhiyong**. Researchers, developers and robotics enthusiasts are welcome to work together to improve the project.

## Participate in discussions

- [Discord Community](https://discord.gg/CacMUBaFgJ)
- [Follow the project author on X](https://x.com/liyitengx) on X
- Email: [liyiteng+github@gmail.com](mailto:liyiteng+github@gmail.com)

## Submit a question

Please submit hardware, printing, and assembly questions to [AlohaMini Issues](https://github.com/liyiteng/AlohaMini/issues). Please submit software issues to [lerobot_alohamini Issues](https://github.com/liyiteng/lerobot_alohamini/issues).

Describing the robot model, reproduction steps and actual phenomenon, and attaching relevant logs or photos can help others locate the problem faster.

## Contribute content

You can correct documentation, add assembly experience, share experimental results, or submit hardware and software improvements. Participate through a Pull Request to the corresponding GitHub repository.

## Acknowledgments

The project builds on the work of the open robotics community, thanks to projects such as ALOHA, LeKiwi, SO-ARM100, LeRobot and Hugging Face.


## Help improve the official tutorial

Documentation contributions can focus on the following:

- Supplement the before and after photos of a certain step and the parts direction instructions.
- Document printing materials, slicing settings, and assembly fit issues.
- Check the actual model and command parameters, and supplement the expected output.
- Submit reproducible installation or device configuration issues and resolution procedures.
- Share data collection and evaluation conditions so experimental results can be compared.

When submitting modifications, please indicate the applicable model, software version, and verification conditions. For parameters such as servo model, power supply, nominal load, etc., corresponding information or test conditions should be attached.

## What should problem feedback include?

Hardware questions give part names, dimensions, materials, printing parameters, assembly locations, and photos. Software problems provide both end systems, submitted versions, complete commands and logs. For specific templates, see [Debugging and troubleshooting](troubleshooting.md).

When reporting tutorial errors, point out the page, chapter, specific steps and your actual measurement results, which can help the maintainer directly correct the corresponding steps.

## Document Maintenance Instructions

The tutorials on this site are organized based on the documents and related codes of the local hardware warehouse `17c6a98` and software repository `7843e588`. Building and page checking are completed locally; robot movement, model training and OpenPI access still need to be verified on the corresponding device.

The currently checked compatibility differences include: model constants of the old independent servo script, OpenPI old client interface, and ROS 2 construction method of the simulation package. Relevant sections are marked so that these differences are not hidden in common commands.

When maintaining the page, simultaneously modify the navigation, chapter cross-links, and parameter tables. After the software interface is updated, priority will be given to reviewing the main lines of installation, calibration, teleoperation, recording, training and evaluation.
