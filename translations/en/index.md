---
html_theme.sidebar_secondary.remove: true
---

# AlohaMini

An open-source mobile robot with two arms for embodied AI research and education.

Connect your robot and teleoperate it. Then collect demonstrations and train a policy.

## Choose your robot

```{raw} html
<div class="am-paths am-models">
<a class="am-path" href="alohamini2.html"><span class="am-model-label">3D printed chassis · STS3215</span><strong>AlohaMini 2 <span aria-hidden="true">→</span></strong><p>Set up your robot, teleoperate it and save your first demonstration.</p><span class="am-model-entry">Start the guide →</span></a>
<a class="am-path" href="alohamini2pro.html"><span class="am-model-label">Reinforced metal chassis · STS3250</span><strong>AlohaMini 2 Pro <span aria-hidden="true">→</span></strong><p>Follow the same steps with commands matched to Pro hardware.</p><span class="am-model-entry">Start the guide →</span></a>
</div>
```
```{raw} html
<figure class="am-hero"><img src="_static/media/assembled2.png" width="1344" height="768" alt="AlohaMini is a first-generation white double-arm mobile robot equipped with lifting columns and wheeled chassis." fetchpriority="high"><figcaption>AlohaMini 1. The second generation uses AM-ARM200 arms and a reinforced mobile chassis.</figcaption></figure>
```

## Building your robot?

For the standard 2, start with [Assembly](assembly.md): prepare the parts and printed components, then follow the illustrated steps. For Pro, check the [hardware configuration](hardware-pro.md) first.

## Teleoperation already works?

Continue with [Data collection](learning.md). Review your recordings before training a policy and evaluating it on hardware.

```{raw} html
<div class="am-resource-row"><a href="yuque/videos.html">Watch demos</a><a href="community.html">Community and support</a><a href="specifications.html">Specifications</a></div>
```

```{raw} html
<div class="am-project-links" aria-label="Project resources">
<a href="https://github.com/liyiteng/AlohaMini" aria-label="GitHub: AlohaMini project"><img src="_static/external-images/551432bacb6b817efe56.svg" alt="GitHub AlohaMini" height="24"></a>
<a href="https://github.com/liyiteng/AlohaMini/stargazers" aria-label="Check out AlohaMini’s GitHub Stars"><img src="_static/external-images/889a2f18c066ae68827c.svg" alt="GitHub Stars" height="24"></a>
<a href="https://x.com/liyitengx" aria-label="Follow @liyitengx on X"><img src="_static/external-images/08ffe2473ce53b7e3838.svg" alt="Follow @liyitengx" height="24"></a>
<a href="https://github.com/liyiteng/AlohaMini/blob/main/LICENSE" aria-label="Apache 2.0 Open Source License"><img src="_static/external-images/96ae2a5e24552c3ad0ae.svg" alt="License Apache 2.0" height="24"></a>
<a href="https://discord.gg/CacMUBaFgJ" aria-label="Join the AlohaMini Discord community"><img src="_static/external-images/5f408227afa1a4f9eae3.svg" alt="Discord Join Chat" height="24"></a>
</div>
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Get started

quickstart
specifications
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Model tutorials

alohamini2
alohamini2pro
hardware-pro
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Build AlohaMini 2

bom
printing
assembly
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Setup and operation

software
configuration
calibration
teleoperation
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Data and learning

learning
training
evaluation
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Advanced tutorials

single-arm
pi05
simulation
runtime
```

```{toctree}
:hidden:
:maxdepth: 2
:caption: Reference and support

commands
troubleshooting
legacy
community
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: Complete tutorials and advanced materials

legacy-hardware
debug-tools
policies
docker
development
video2sim
sim-data
tutorial-library
```

```{toctree}
:hidden:
:maxdepth: 1
:caption: Official delivery tutorial

official-manual
```
