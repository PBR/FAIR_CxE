FROM secoresearch/fuseki
# see https://github.com/SemanticComputing/fuseki-docker

USER root
# admin username for fuseki is admin

RUN mkdir /application
COPY --chown=9008 ./common_files/ /common_files/

# copy all phenotypic (meta)data to a single .ttl, then load it on Fuseki
COPY --chown=9008 /common_files/pheno_setup.ttl /fuseki-base/configuration/pheno_setup.ttl
RUN echo "@base <http://localhost:3030/wur/fair-example> ." > /common_files/all_pheno.ttl
#RUN cat /common_files/data-generated/headless.ttl >> /common_files/all_pheno.ttl
RUN cat /common_files/data-generated/miappe_metadata.ttl >> /common_files/all_pheno.ttl
RUN cat /common_files/data-generated/phenotypic/*.ttl >> /common_files/all_pheno.ttl
RUN $TDBLOADER --tdb /fuseki-base/configuration/pheno_setup.ttl /common_files/all_pheno.ttl 

# copy all weather files to a single ttl, then load it on Fuseki (weather dataset)
COPY --chown=9008 /common_files/weather_setup.ttl /fuseki-base/configuration/weather_setup.ttl
RUN echo "@base <http://localhost:3030/weather-host/fair-example> ." > /common_files/all_weather.ttl
RUN cat /common_files/data-generated/weather/*.ttl >> /common_files/all_weather.ttl
RUN cat /common_files/data-generated/station_metadata.ttl >> /common_files/all_weather.ttl
RUN $TDBLOADER --tdb /fuseki-base/configuration/weather_setup.ttl /common_files/all_weather.ttl 
