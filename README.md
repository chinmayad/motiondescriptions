Here's an edited version of the readme file to improve readability:

---

# Motion Description Dataset

To obtain motion descriptions, we use the GPT-4 API. For detailed evaluation of the quality of data and the dataset statistics, please refer to the file **User_Study_Dataset Statistics.pdf**.

This dataset is provided in conjunction with the HMDB51, UCF101, and Kinetics-400 datasets. We encourage users to download the videos from their respective official pages and use the motion descriptions provided in this repository.

## Datasets

### HMDB51 Dataset
- **HMDB51_without_objectname.csv**: Motion descriptions without object names.
- **hmdb51_motion_with_objectname.csv**: Motion descriptions with object names.
- **hmdb_descriptions.csv**: Action descriptions.
- **hmdb51_motion_alternate_version.csv**: Alternate motion description file not used in our experiments.

### UCF101 Dataset
- **ucf101_without_objectname.csv**: Motion descriptions without object names.
- **uc101_motion.csv**: Motion descriptions with object names.
- **ucf_descriptions.csv**: Action descriptions.
- **ucf_motion_alternate_version.csv**: Alternate motion description file not used in our experiments.

### Kinetics-400 Dataset
- **kinetics400_motion_descriptions.csv**: Motion descriptions.
- **Kinetics400_action_descrptions.csv**: Action descriptions.

**Note**: Motion descriptions describe the motion in the action, whereas action descriptions describe the action itself.

## Code
The code will be released soon.

## Citation
If you find this dataset useful in your research, please consider citing:

```bibtex
@article{devaraj2024diving,
  title={Diving Deep into the Motion Representation of Video-Text Models},
  author={Devaraj, Chinmaya and Fermuller, Cornelia and Aloimonos, Yiannis},
  journal={arXiv preprint arXiv:2406.05075},
  year={2024}
}
```

---
