%%% Script de ejemplo de Newton Rapson

    clear; clc; close all;
    
    ejex=-5:0.1:5; % Visualización de puntos de entreamiento y resultado
    %%%%% Ejemplo de funcion cuadrática con Newton Rapson
    % Valores iniciales y funcion
            x0=-4;
            f=-ejex.^2+3*ejex+3;
        %Graficado
            plot(ejex,f); hold on;
            xlabel('x')
            ylabel('f(x)')
                            
            x=x0;
            error=10;
            xnextvector=x0;
           %Iteraciones del método numérico 
                while abs(error)>0.0001
                    xnext=x-(-x.^2+3*x+3)/(-2*x+3); %Funcion evaluada
                    error = xnext-x                    %Variación entre valores de x (máximo)
                    x= xnext
                    xnextvector=[xnextvector xnext];  %Concatenacion de vector para graficar convergencia del algoritmo
                end
        %%% Graficado de los resultados del método numérico
                figure; 
                plot(xnextvector,'o-')
                xlabel('n')
                ylabel('x_n_+_1')
 
%Newton Rapson para el caso de Logistic Regression
        %training points
       %%%%%%%%% Set para clase %%%%%%%%%%%%%%%%%%%
                %x = [1 -0.1 -0.5 -2 2 2.3 4 0 5 ];
                x = [-0.1 -0.5 -2 2 2.3 4 0 5 ];
            %Normalizando datos por medio de la resta de la media
                media = mean(x);
                x = x - media;%             
%                 y= [1 1 1 1 0 0 0 0 0];
                %y= [ 0 0 0 0 0 1 1 1 1];
                y= [ 0 0 0 1 1 1 1 1 ];
    
    %%%%%%%%%Set de basket
    %%%%%%%%%https://towardsdatascience.com/understanding-logistic-regression-using-a-simple-example-163de52ea900 
    
        
        %Numerical method for m estimation
        
            error=10;
            minitial=5;
            m=minitial
            mplot=m;
    %%% se repite el ciclo para el caso de regresion logística, diapositiva 15            
          while abs(error)>0.05

                mnext=m - sum((y -logisticf(x,m,0)).*x )/sum(-(x.*logisticf(x,m,0)).*(1-logisticf(x,m,0)) - logisticf(x,m,0))
                error = mnext-m
                m= mnext
                mplot = [mplot m];
          end
    %%% Graficado de resultados de convergencia     
      figure;
      stem(mplot)
      legend('m value')
   %%% Graficado de la clasificacion de datos   
      figure;
      plot(ejex,logisticf(ejex,m,media)); hold on
      stairs(x,y,'r*')
      legend('Logistic classification','inputs')
      xlabel('x')
      ylabel('y')
        
            
            
            
            
            
            
