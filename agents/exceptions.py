class ATSAgentError(Exception):
    """Base exception for ATS Resume AI Agent."""
    pass


class GeminiAPIError(ATSAgentError):
    """Raised when Gemini API fails."""
    pass


class InvalidJSONError(ATSAgentError):
    """Raised when Gemini returns invalid JSON."""
    pass


class ResumeValidationError(ATSAgentError):
    """Raised when resume validation fails."""
    pass


class FileReadError(ATSAgentError):
    """Raised when a resume or job description file cannot be read."""
    pass