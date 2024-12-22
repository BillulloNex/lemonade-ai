from llmware.models import ModelCatalog  

tool = 'slim-sa-ner-tool'
# to load the model and make a basic inference
model = ModelCatalog().load_model(tool)
response = model.function_call('hello, how are you?')  

# this one line will download the model and run a series of tests
ModelCatalog().tool_test_run(tool, verbose=True)
