# Oral ESP - Homosexualidad en el cine cubano (opción 2)

Deck as code para el segundo oral de **Español Intermedio LES 51201**.

- **Opción**: un tema hispánico a través de dos películas
- **Tema**: la representación de la homosexualidad en Cuba
- **Corpus**: *Fresa y chocolate* (1993) · *Antes que anochezca* (2000)
- **Plantilla**: `assets/Template_X.pptx` (École polytechnique)
- **Extractos**: 2 clips incrustados (35 s cada uno), carteles = plan B
- **Interacción**: planche 12 « Preguntas para ustedes »

## Build

```bash
uv sync
uv run python scripts/render.py check
uv run python scripts/render.py all
```

Livrable: `build/Presentation_ESP_Cuba_Homosexualidad_Cine_Ivann_KAMDEM.pptx`
