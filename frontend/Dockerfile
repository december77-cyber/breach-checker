FROM nginx:alpine
COPY index.html style.css script.js /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf
RUN date > /usr/share/nginx/html/build.txt