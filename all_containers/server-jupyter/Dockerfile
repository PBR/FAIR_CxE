#FROM python:3.7
FROM python:3.7-slim-buster

USER root

WORKDIR /usr/src/app
COPY ./common_files .
RUN ls
RUN python3 -m pip install --upgrade pip ipython ipykernel
RUN pip3 install --no-cache-dir -r requirements_jupyter.txt
RUN pip3 install jupyter jupyter_contrib_nbextensions

RUN jupyter contrib nbextension install --user
RUN jupyter nbextension enable codefolding/main
RUN jupyter nbextension enable toggle_all_line_numbers/main
RUN jupyter nbextension enable collapsible_headings/main
RUN jupyter nbextension enable toc2/main

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents
# kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["jupyter", "notebook", "--port=8888", "--no-browser", "--ip=0.0.0.0", "--allow-root"]
