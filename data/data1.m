csvfile = "C:\Users\Tom K\Google Drive\Programs\courses\Computing\exoplanetsclean";
exo = readtable(csvfile);
exo.Name = string(exo.Name);
hold on
scatter(exo.Mass(exo.Habitable==1),exo.Orbit(exo.Habitable==1))
xlabel('Planetary Mass (EU)')
ylabel('Orbital Radius (AU)')
title("Habitable Exoplanets")
hold off