h=figure;
nodes = 1.5;
x = 0:0.01:6.28;
axis([0 2*pi -1.5 1.5])
ax = gca;
ax.NextPlot = 'replaceChildren';
loops =80;
M1(loops) = struct('cdata',[],'colormap',[]);
h.Visible = 'off';
for k = 1:loops
    fact = sin(k*pi/10);
    plot(x,fact*sin(nodes*x),'r')
    drawnow
    M1(k) = getframe;
end
h.Visible = 'on';
movie(M1)