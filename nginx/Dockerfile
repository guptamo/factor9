FROM nginx:1.10-alpine
MAINTAINER goeast

RUN rm /etc/nginx/conf.d/default.conf
COPY factor9.ca.conf /etc/nginx/conf.d/factor9.ca.conf
RUN ls /etc/nginx/conf.d
