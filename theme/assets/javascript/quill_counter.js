
class Counter {
    constructor(quill, options) {
      this.quill = quill;
      this.options = options;
      this.container = document.querySelector(options.container);
      quill.on(Quill.events.TEXT_CHANGE, this.update.bind(this));
    }
  
    calculate() {
      const text = this.quill.getText();
  
      if (this.options.unit === 'word') {
        const trimmed = text.trim();
        // Splitting empty text returns a non-empty array
        return trimmed.length > 0 ? trimmed.split(/\s+/).length : 0;
      } else {
        return text.length;
      }
    }
  
    update() {
      const length = this.calculate();
      //let label = this.options.unit;
      //if (length !== 1) {
      //  label += '4';
      //}
      //this.container.innerText = `${length} ${label}`;
      this.container.innerText = `${length}`;
    }
  }
  
  Quill.register('modules/counter', Counter);