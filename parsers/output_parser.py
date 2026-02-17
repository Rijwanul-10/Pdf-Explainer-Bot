from langchain_core.output_parsers import PydanticOutputParser
from schemas.models import LLMResponse

parser = PydanticOutputParser(pydantic_object=LLMResponse)
