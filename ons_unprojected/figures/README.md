# Extension figure

Edit `extension.tex`, which contains the standalone TikZ/PGFPlots source.
From the `ons_unprojected` directory, rebuild the vector PDF with:

```sh
make -C figures
```

The manuscript includes `extension.pdf` at its natural size. Normal manuscript
builds reuse this PDF without compiling the figure again. After editing the
figure, run the command above before rebuilding the manuscript. Keep both the
source and PDF in version control so the manuscript can compile directly.

The standalone document uses the manuscript's 12-point base font size and Times
text font, with no added border, to preserve the figure's size and labels.
