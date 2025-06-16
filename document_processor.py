import asyncio
from kreuzberg import extract_file
import magic
import os
from datetime import datetime

class DocumentProcessor:
    def __init__(self):
        """Initialize the document processor with Kreuzberg"""
        pass
    
    
    async def extract_text_with_kreuzberg(self, file_path):
        """Extract text using Kreuzberg's extract_file function"""
        try:
            result = await extract_file(file_path)
            
            # Extract relevant information from Kreuzberg result
            return {
                'text': result.content if hasattr(result, 'content') else str(result),
                'confidence': getattr(result, 'confidence', 100),
                'method': 'Kreuzberg',
                'metadata': getattr(result, 'metadata', {}),
                'page_count': getattr(result, 'page_count', 1)
            }
            
        except Exception as e:
            return {
                'text': '',
                'confidence': 0,
                'method': 'Kreuzberg',
                'error': str(e)
            }
  