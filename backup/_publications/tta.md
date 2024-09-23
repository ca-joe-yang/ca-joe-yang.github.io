---
title: "Deep Nets with Subsampling Layers Unwittingly Discard Useful Activations at Test-Time"
collection: publications
permalink: /publication/tta
excerpt: 'Subsampling layers play a crucial role in deep nets by discarding a portion of an activation map to reduce its spatial dimensions. This encourages the deep net to learn higher-level representations. Contrary to this motivation, we hypothesize that the discarded activations are useful and can be incorporated on the fly to improve models' prediction. To validate our hypothesis, we propose a search and aggregate method to find useful activation maps to be used at test-time. We applied our approach to the task of image classification and semantic segmentation. Extensive experiments over nine different architectures on ImageNet, CityScapes, and ADE20K show that our method consistently improves model test-time performance. Additionally, it complements existing test-time augmentation techniques to provide further performance gains.'
date: 2024
venue: 'ECCV'
# slidesurl: 'http://academicpages.github.io/files/slides3.pdf'
# paperurl: 'http://academicpages.github.io/files/paper3.pdf'
# citation: 'Your Name, You. (2015). &quot;Paper Title Number 3.&quot; <i>Journal 1</i>. 1(3).'
---

The contents above will be part of a list of publications, if the user clicks the link for the publication than the contents of section will be rendered as a full page, allowing you to provide more information about the paper for the reader. When publications are displayed as a single page, the contents of the above "citation" field will automatically be included below this section in a smaller font.