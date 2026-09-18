from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Smart Energy"
    database_url: str = "sqlite:///./smart_energy.db"
    jwt_secret: str = "development-secret"
    otp_provider: str = "mock"
    email_provider: str = "mock"
    sms_provider: str = "mock"
    open_meteo_url: str = "https://api.open-meteo.com/v1/forecast"
    frontend_url: str = "http://localhost:5173"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
