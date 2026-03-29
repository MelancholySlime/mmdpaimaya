# mmdpaimaya v3.1.2

A Maya script for importing MMD models into Maya and exporting Maya-built models to MMD format (`.pmx`).

## Features

- **MMD → Maya**: Import `.pmx`, `.pmd`, and `.x` model files into Maya, with optional bone, blend shape, and material creation
- **Maya → MMD**: Export Maya meshes back to `.pmx` format
- **Human IK Manager**: Automatically define and map MMD joints to Maya's Human IK system
- **English bone names**: All imported joints use **League of Legends-style naming** (`L_Shoulder`, `R_Hand`, `Spine1`, `Pelvis`, etc.)
- **Smart name translation**: Unknown custom bones (hair, skirt, accessories, physics) are decomposed and translated component-by-component (e.g. `kamihidari1` → `L_Hair1`, `sukaatousiro1` → `SkirtBack1`)

## Supported Maya Versions

| Version | Package |
|---------|---------|
| Maya 2022 – 2025 | This repo (`v3.1.2`) |
| Maya 2015 – 2018 | Use `v2.0.2` (see zip included) |

## Installation

1. Copy the `mmdpaimaya` folder into your Maya scripts folder:
   - **Windows**: `Documents\maya\<version>\scripts\`
   - **Mac / Linux**: `~/maya/<version>/scripts/`

2. In Maya's Script Editor (Python tab), run:

```python
import mmdpaimaya
mmdpaimaya.run()
```

## Usage

### Import (MMD → Maya)

1. Click **MMD > Maya (Import)**
2. Select a `.pmx`, `.pmd`, or `.x` file (or drag & drop it)
3. Set scale and options, then click **Start Import**

### Export (Maya → MMD)

1. Click **Maya > MMD (Export)**
2. Choose the output `.pmx` path
3. Configure options, then click **Start Export**

### Human IK

1. Click **Manage Human IK**
2. Select the imported mesh from the dropdown
3. Click **Define** — joints will be auto-mapped
4. Click **Create Control Rig** to finish


## Original Information

- **Author**: [phyblas](https://qiita.com/phyblas)
- **Original guide** (Japanese): https://qiita.com/phyblas/items/e5fe203c955e273b26a4
- **This fork adds**: English UI, LoL-style bone renaming, component-based name translation

![](https://phyblas.hinaboshi.com/rup/yami/2018/a04.jpg)