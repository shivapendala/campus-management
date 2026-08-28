import React, { useState } from 'react';

const StepperForm = ({
  steps = [], // [{ title: 'Step 1', subtitle: '...', content: ReactNode, validate: () => boolean }]
  onComplete = () => {},
  submitButtonText = 'Submit',
  isSubmitting = false
}) => {
  const [currentStep, setCurrentStep] = useState(0);

  const handleNext = () => {
    const step = steps[currentStep];
    if (step.validate && !step.validate()) {
      return;
    }
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      onComplete();
    }
  };

  const handlePrev = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  return (
    <div className="stepper-form-card card border-0 shadow-sm rounded-3 p-4">
      {/* Step Indicators Header */}
      <div className="d-flex justify-content-between align-items-center mb-4 position-relative">
        <div
          className="position-absolute top-50 start-0 w-100 bg-secondary-subtle"
          style={{ height: '2px', zIndex: 1, transform: 'translateY(-50%)' }}
        ></div>
        <div
          className="position-absolute top-50 start-0 bg-primary transition-all"
          style={{
            height: '2px',
            zIndex: 2,
            transform: 'translateY(-50%)',
            width: `${(currentStep / (steps.length - 1 || 1)) * 100}%`,
          }}
        ></div>

        {steps.map((step, idx) => {
          const isDone = idx < currentStep;
          const isActive = idx === currentStep;

          return (
            <div key={idx} className="d-flex flex-column align-items-center position-relative" style={{ zIndex: 3 }}>
              <div
                className={`rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm ${
                  isDone
                    ? 'bg-success text-white'
                    : isActive
                    ? 'bg-primary text-white ring'
                    : 'bg-light text-muted border'
                }`}
                style={{ width: '40px', height: '40px' }}
              >
                {isDone ? <i className="bi bi-check-lg"></i> : idx + 1}
              </div>
              <span className={`small mt-2 ${isActive ? 'fw-bold text-primary' : 'text-muted'}`}>
                {step.title}
              </span>
            </div>
          );
        })}
      </div>

      {/* Step Body Content */}
      <div className="step-body-content py-3 min-vh-25">
        <h5 className="fw-bold mb-1">{steps[currentStep]?.title}</h5>
        {steps[currentStep]?.subtitle && (
          <p className="text-muted small mb-3">{steps[currentStep].subtitle}</p>
        )}
        <div>{steps[currentStep]?.content}</div>
      </div>

      {/* Footer Navigation Buttons */}
      <div className="d-flex justify-content-between align-items-center border-top pt-3 mt-4">
        <button
          type="button"
          className="btn btn-outline-secondary px-4"
          onClick={handlePrev}
          disabled={currentStep === 0 || isSubmitting}
        >
          <i className="bi bi-arrow-left me-1"></i>Previous
        </button>

        <button
          type="button"
          className="btn btn-primary px-4"
          onClick={handleNext}
          disabled={isSubmitting}
        >
          {isSubmitting ? (
            <>
              <span className="spinner-border spinner-border-sm me-2" role="status"></span>
              Processing...
            </>
          ) : currentStep === steps.length - 1 ? (
            <>
              <i className="bi bi-check2-circle me-1"></i>
              {submitButtonText}
            </>
          ) : (
            <>
              Next<i className="bi bi-arrow-right ms-1"></i>
            </>
          )}
        </button>
      </div>
    </div>
  );
};

export default StepperForm;
