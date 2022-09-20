from loko_extensions.model.components import Component, Input, Output, save_extensions

d_in = Input(id="input",
          label="predict",
          service="image/predict",
          to="output")

d_out = Output(id="output",label="predict")


c = Component(name="NN Simple IMG CLF", inputs=[d_in], outputs=[d_out])

save_extensions([c])




