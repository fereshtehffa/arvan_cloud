FROM ubuntu:18.04

RUN    echo "deb-src http://archive.ubuntu.com/ubuntu bionic main" >> /etc/apt/sources.list
RUN    sed 's/main$/main universe/' /etc/apt/sources.list 
RUN    apt update
RUN    apt -y upgrade
RUN    apt install -y wget git


# Openresty (Nginx)
RUN    apt -y build-dep nginx
RUN    wget https://openresty.org/download/openresty-1.17.8.2.tar.gz
RUN    tar xvfz openresty-1.17.8.2.tar.gz
RUN    cd openresty-1.17.8.2 ; ./configure --with-luajit  --with-http_addition_module --with-http_dav_module --with-http_gzip_static_module --with-http_image_filter_module --with-http_realip_module --with-http_stub_status_module --with-http_ssl_module --with-http_sub_module --with-http_xslt_module --with-pcre-jit;  make ; make install

EXPOSE 8080
RUN mkdir /logs/
RUN    git clone https://github.com/ledgetech/lua-resty-http.git /opt/lua-resty-http
RUN    git clone https://github.com/fereshtehffa/lua-aws.git /opt/lua-aws
RUN    git clone https://github.com/mpx/lua-cjson.git /opt/lua-cjson
COPY nginx.conf /
COPY app.lua /
CMD /usr/local/openresty/nginx/sbin/nginx -p `pwd` -c nginx.conf
