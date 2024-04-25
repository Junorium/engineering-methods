% data points
% values of the independent variable
x = [0.8690    1.7627    2.2169    2.9545    3.4162    4.1227    4.5885    5.1963    6.0032    6.5000];
% values of the dependent variable
y = [0.8912    1.9208    0.6152    0.8308    0.2818    0.0363    0.3111    1.5688    0.4521    0.2265];

% query value of the independent variable
x_min = min(x);
x_max = max(x);
x_interp = x_min + rand() * (x_max - x_min);

% compute index using find function
index = 1;

while ~(x_interp >= x(index) && x_interp < x(index+1))
    index = index + 1;
end
index_find = find(x_interp<x);
index_find = index_find(1) - 1;

% compute the slope
m = (y(index + 1) - y(index)) ./ (x(index+1) - x(index));

% compute y-intercept
n = y(index) - m.*x(index);

% compute the predicted value of the dependept variable
y_interp = m*x_interp + n;
